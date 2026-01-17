from analyzer import analyze_code
from llm_offline import convert_code
from postprocessor import clean_code

FILE_PATH = "samples/legacy_java.java"


def main():
    print("🔍 Analyzing code...")

    if FILE_PATH.endswith(".py"):
        errors = analyze_code(FILE_PATH)
    else:
        errors = ["Analyzer skipped (non-Python source file)"]

    if errors:
        print("Errors found:")
        for e in errors:
            print(e)

    with open(FILE_PATH, "r") as f:
        legacy_code = f.read()

    print("\n🤖 Converting code using offline LLM...")
    converted = convert_code(legacy_code)

    print("\n🧹 Cleaning code...")
    final_code = clean_code(converted)

    print("\n✅ Final Output:\n")
    print(final_code)


if __name__ == "__main__":
    main()

