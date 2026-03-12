# error_rules.py

ERROR_EXPLANATIONS = {
    "NullPointerException": {
        "explanation": "Occurs when your code tries to use an object that is null.",
        "causes": [
            "Object not initialized",
            "Method returned null",
            "Dependency injection failed"
        ],
        "fix": "Check for null before calling methods."
    },
    "KeyError": {
        "explanation": "Occurs when you access a dictionary key that does not exist.",
        "causes": [
            "Key is missing in the dictionary",
            "Dictionary was empty"
        ],
        "fix": "Use dict.get() or check if key exists."
    },
    "CrashLoopBackOff": {
        "explanation": "Kubernetes failed to start the container repeatedly.",
        "causes": [
            "Container startup failed",
            "Configuration error",
            "Memory/resource limits exceeded"
        ],
        "fix": "Check container logs and fix configuration."
    }
}