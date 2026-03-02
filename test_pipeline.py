from main import reliability_layer

# LLM Feed
user_input = "Severe fire but no visible damage today"

# Readable Output (Temporary)
def pretty_print(text, result):

    print("\n================ INCIDENT REPORT =================")
    print(f"Original Input    : {text}")

    validated = result.get("validated_output")

    # Case 1 : RELIABILITY LAYER REJECTED THE INCIDENT

    if validated is None:

        print("\n⚠️  REPORT REJECTED BY RELIABILITY LAYER")
        print("Reason: Unsafe or Low Confidence Repair")

        errors = result.get("validation_errors") or []
        if errors:
            print("\nValidation Errors:")
            for e in errors:
                print("  -", e)

        print(f"\nFinal Confidence  : {result.get('confidence')}")
        print("==================================================\n")
        return

    # Case 2 : SUCCESSFUL STRUCTURED OUTPUT

    print(f"\nIncident Type     : {validated.get('incident_type')}")
    print(f"Severity          : {validated.get('severity')}")
    print(f"Incident Time     : {validated.get('incident_time')}")
    print(f"Report Time       : {validated.get('report_time')}")
    print(f"Location          : {validated.get('city')}, {validated.get('state')}")

    print(f"\nMissing Fields    : {result.get('missing_fields')}")

    print("\nConsistency Errors:")
    if result.get("consistency_errors"):
        for e in result["consistency_errors"]:
            print("  -", e)
    else:
        print("  None")

    print("\nConsistency Warnings:")
    if result.get("consistency_warnings"):
        for w in result["consistency_warnings"]:
            print("  -", w)
    else:
        print("  None")

    print(f"\nFinal Confidence  : {result.get('confidence')}")
    print("==================================================\n")


result = reliability_layer(user_input)
pretty_print(user_input, result)
