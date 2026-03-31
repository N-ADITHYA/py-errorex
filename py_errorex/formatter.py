def format_output(result, error_info):
    print("\n❌ " + error_info["message"])
    print("👉 " + result["explanation"])

    print(f"\n📍 File: {error_info['file']}")
    print(f"🔢 Line: {error_info['line']}")
    print(f"👉 Code: {error_info['code']}")

    print("\n💡 Why:")
    print(result["why"])

    print("\n👉 Fixes:")
    for fix in result["fixes"]:
        print(" - " + fix)