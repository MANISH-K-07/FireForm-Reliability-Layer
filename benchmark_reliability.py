from fireform.extraction.mock_extractor import extract_incident_data
from fireform.reliability.missing import detect_missing_fields
from fireform.reliability.validator import validate_incident
from fireform.reliability.recoverability import classify_recoverability
from generate_inputs import generate_dataset
from main import reliability_layer


print("\n=========== RUNNING TRUE BENCHMARK ===========\n")

n = 150

test_inputs = generate_dataset(n)
total = len(test_inputs)

# ---------------- RAW COUNTERS ----------------
raw_failures = 0
raw_validation_errors = 0
salvageable_raw = 0
unrecoverable_raw = 0

# ---------------- RELIABILITY COUNTERS ----------------
structured_success = 0
reliable_validation_errors = 0
consistency_warnings = 0
post_layer_recovered = 0
unsafe_guess = 0


for text in test_inputs:

    # ---------------- RAW EXTRACTION ----------------
    raw = extract_incident_data(text)

    missing = detect_missing_fields(raw)
    raw_validated, raw_errors = validate_incident(raw)

    if missing:
        raw_failures += 1

    if raw_errors:
        raw_validation_errors += 1

    # ---------------- RECOVERABILITY ----------------
    recoverability = classify_recoverability(raw)

    if recoverability == "salvageable":
        salvageable_raw += 1
    else:
        unrecoverable_raw += 1

    # ---------------- RELIABILITY LAYER ----------------
    result = reliability_layer(text)

    validated = result.get("validated_output")

    raw_error_count = len(raw_errors) if raw_errors else 0
    new_errors = result.get("validation_errors")
    new_error_count = len(new_errors) if new_errors else 0

    # Repair success ONLY for salvageable cases
    if recoverability == "salvageable":
        if new_error_count < raw_error_count:
            post_layer_recovered += 1

    # Structured success
    if validated and new_error_count == 0:
        structured_success += 1

    if result["validation_errors"]:
        reliable_validation_errors += 1

    if result.get("consistency_warnings"):
        consistency_warnings += 1


print("Total Test Cases                  :", total)

print("\n--------------- RAW EXTRACTION ---------------")
print("Missing Field Cases               :", raw_failures)
print("Validation Error Cases            :", raw_validation_errors)

print("\n----------- WITH RELIABILITY LAYER -----------")
print("Structured Success Cases          :", structured_success)
print("Validation Error Cases            :", reliable_validation_errors)
print("Consistency Warnings Raised       :", consistency_warnings)

print("\n------------------ METRICS -------------------")
print(f"Raw Missing Rate                  : {(raw_failures/total)*100:.2f}%")
print(f"Raw Validation Error Rate         : {(raw_validation_errors/total)*100:.2f}%")
print(f"Post-Layer Success Rate           : {(structured_success/total)*100:.2f}%")

print("\n----------- RECOVERABILITY METRICS -----------")
print(f"Salvageable Raw Cases             : {salvageable_raw}")
print(f"Unrecoverable Raw Cases           : {unrecoverable_raw}")
print(f"Post-Layer Recovered Cases        : {post_layer_recovered}")
print("")

if salvageable_raw > 0:
    repair_rate = (post_layer_recovered / salvageable_raw) * 100
    print(f"Effective Repair Rate             : {repair_rate:.2f}%")

print(f"Unsafe Guess Count                : {unsafe_guess}")
print("----------------------------------------------\n")
