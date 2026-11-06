import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_ROOT)


def check_and_prepare_artifacts():
    print("=" * 70)
    print("Self-Explaining Wireless IDS - Startup")
    print("=" * 70)

    model_path = os.path.join(
        PROJECT_ROOT, "backend", "models", "baseline_rf.joblib"
    )

    if not os.path.exists(model_path):
        print("[!] Model artifacts missing. Training model...")
        from scripts.train_model import train_and_evaluate_model
        train_and_evaluate_model()
    else:
        print("[+] Model artifacts found.")

    samples_dir = os.path.join(PROJECT_ROOT, "data", "samples")

    if not os.path.exists(samples_dir) or not os.listdir(samples_dir):
        print("[!] Sample data missing. Generating...")
        from scripts.generate_synthetic_scenarios import generate_all_samples
        generate_all_samples()
    else:
        print("[+] Sample data found.")

    db_file = os.path.join(
        PROJECT_ROOT, "backend", "wireless_ids.db"
    )

    if not os.path.exists(db_file):
        print("[!] Database missing. Seeding...")
        from scripts.seed_database import seed
        seed()
    else:
        print("[+] Database found. Skipping seed.")


def run_server():
    check_and_prepare_artifacts()

    import uvicorn

    port = int(os.environ.get("PORT", 8000))

    uvicorn.run(
        "backend.app.main:app",
        host="0.0.0.0",
        port=port,
        reload=False
    )


if __name__ == "__main__":
    run_server()
