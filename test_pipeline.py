from main import reliability_layer

# LLM Feed
user_input = "Severe fire but no visible damage today"

# Readable Output (Temporary)
def pretty_print(user_input, result):

    print("\n================ INCIDENT REPORT =================")

    print(f"Original Input    : {user_input}")

    validated = result.get("validated_output", {})

    print(f"\nIncident Type     : {validated.get('incident_type')}")
    print(f"Severity          : {validated.get('severity')}")
    print(f"Incident Time     : {validated.get('incident_time')}")
    print(f"Report Time       : {validated.get('report_time')}")

    location = validated.get("location", {})
    print(f"Location          : {location.get('city')}, {location.get('state')}")

    print("\nMissing Fields    :", result.get("missing_fields"))

    print("\nConsistency Errors:")
    if result.get("consistency_errors"):
        for err in result["consistency_errors"]:
            print("  -", err)
    else:
        print("  None")

    print("\nConsistency Warnings:")
    if result.get("consistency_warnings"):
        for warn in result["consistency_warnings"]:
            print("  -", warn)
    else:
        print("  None")

    print(f"\nFinal Confidence  : {result.get('confidence')}")
    print("==================================================\n")


result = reliability_layer(user_input)
pretty_print(user_input, result)
