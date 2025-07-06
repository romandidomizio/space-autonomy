"""
Main entry point for the AegisNav system.

This script will initialize the agentic workflow and start the Streamlit UI.
"""

from ui.dashboard import run_dashboard

def main():
    print("Initializing AegisNav..."_)
    run_dashboard()

if __name__ == "__main__":
    main()
