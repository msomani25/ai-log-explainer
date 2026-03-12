import os
import anthropic

# ---------------------------
# Local rule-based explanation
# ---------------------------
def explain_log_locally(log):
    """
    Local rule-based log explanation.
    Detects Java NullPointerException, Python KeyError, and Docker container errors.
    """
    log_lower = log.lower()  # lowercase for safer matching

    # --- Java error ---
    if "nullpointerexception" in log_lower:
        return {
            "error": "NullPointerException",
            "explanation": "The code tried to use an object that was null.",
            "fix": "Check where the object should be initialized or add null checks."
        }

    # --- Python error ---
    if "keyerror" in log_lower:
        return {
            "error": "KeyError",
            "explanation": "Python tried to access a dictionary key that does not exist.",
            "fix": "Check if the key exists before accessing it."
        }

    if "indexerror" in log_lower:
    	   return {
        	  "error": "IndexError",
        	  "explanation": "Python tried to access a list element that does not exist.",
        	  "fix": "Make sure the index is within the list length."
    	   }

    # --- Docker error ---
    if "crashloopbackoff" in log_lower or "back-off restarting" in log_lower:
        return {
            "error": "Docker container crash",
            "explanation": "The container failed to start due to configuration or environment issues.",
            "fix": "Check container configuration, image, and environment variables."
        }

    # --- Unknown / fallback ---
    return {
        "error": "Unknown",
        "explanation": "Could not detect error locally.",
        "fix": "Try AI explanation (select option 2) if available."
    }

# ---------------------------
# AI explanation using Claude
# ---------------------------
def explain_log_with_ai(log):
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        return "Claude API key not found. Please set ANTHROPIC_API_KEY in your environment."

    try:
        client = anthropic.Anthropic(api_key=api_key)

        # Use a model available to your account
        model_name = "claude-opus-4-6"

        response = client.messages.create(
            model=model_name,
            max_tokens=200,
            messages=[
                {
                    "role": "user",
                    "content": f"Explain this error log in simple terms and suggest a fix:\n\n{log}"
                }
            ]
        )

        return response.content[0].text

    except anthropic.BadRequestError as e:
        return f"AI explanation failed: {e}"
    except anthropic.NotFoundError:
        return "AI explanation failed: model not available on this account."
    except Exception as e:
        return f"AI explanation failed: {e}"

# ---------------------------
# Load logs from folder
# ---------------------------
def load_logs():
    log_folder = "logs"
    if not os.path.exists(log_folder):
        print("Logs folder not found!")
        return ""

    files = os.listdir(log_folder)
    if not files:
        print("No log files found!")
        return ""

    print("\nAvailable logs:")
    for i, f in enumerate(files):
        print(f"{i+1}. {f}")

    try:
        choice = int(input("\nSelect log number: ")) - 1
        if choice < 0 or choice >= len(files):
            print("Invalid choice")
            return ""
    except ValueError:
        print("Invalid input")
        return ""

    file_path = os.path.join(log_folder, files[choice])
    with open(file_path) as f:
        return f.read()

# ---------------------------
# Main program
# ---------------------------
def main():
    log = load_logs()
    if not log:
        return

    print("\nChoose explanation mode:")
    print("1. Local rule-based")
    print("2. AI explanation (Claude)")

    mode = input("\nEnter choice: ")

    if mode == "1":
        result = explain_log_locally(log)
        print("\nDetected Error:", result["error"])
        print("Explanation:", result["explanation"])
        print("Suggested Fix:", result["fix"])

    elif mode == "2":
        result = explain_log_with_ai(log)
        print("\nAI Explanation:\n")
        print(result)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()