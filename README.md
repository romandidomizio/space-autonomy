# AegisNav: Agentic Deep-Space Navigation & Anomaly-Resilient Trajectory Planning

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Overview

AegisNav is an AI-powered, agentic autonomy framework for deep-space trajectory planning. It is designed to autonomously plan, simulate, and adjust spacecraft trajectories under realistic orbital conditions. The system can detect mission anomalies, adapt flight paths safely, and align its decisions with pre-defined mission protocols.

This project serves as a high-fidelity simulation environment for developing and testing autonomous systems for interplanetary missions. It leverages NASA's General Mission Analysis Tool (GMAT) for trajectory simulation, LangGraph for orchestrating a multi-agent AI system, and machine learning for real-time anomaly detection. All operations are visualized in a mission control dashboard built with Streamlit.

The primary use case is an autonomous Earth-to-Mars transfer, where the system must respond to mid-course anomalies (e.g., simulated fuel loss or thruster deviations) by replanning its trajectory without human intervention.

## 🧠 System Architecture

The system is composed of several key components that work in concert:

-   **Agentic Core (LangGraph)**: A multi-agent system orchestrates the entire workflow.
    -   `Planner Agent`: Proposes an initial trajectory using mission constraints and historical data retrieved via a RAG pipeline.
    -   `Evaluator Agent`: Validates the proposed trajectory against mission requirements (e.g., delta-v budget, arrival time).
    -   `Monitor Agent`: Continuously observes the spacecraft's state during simulation.
    -   `Anomaly Detection Agent`: Uses a machine learning model (e.g., Isolation Forest or a Temporal Convolutional Network) to identify deviations from the planned trajectory.
    -   `Replanning Agent`: Triggers a new planning cycle if an anomaly is detected and confirmed.
-   **Simulation Engine (GMAT)**: NASA's General Mission Analysis Tool provides high-fidelity orbital mechanics simulation.
-   **Mission Control UI (Streamlit)**: An interactive dashboard for visualizing the trajectory, monitoring agent decisions, and reviewing mission logs.
-   **RAG Pipeline (LlamaIndex + ChromaDB)**: Injects domain knowledge from historical mission documents to inform the Planner Agent's decisions.

![Architecture Diagram](docs/architecture.png)  <!-- Placeholder for diagram -->

## 🛠️ Tech Stack

| Category                  | Technology                                      | Purpose                                                 |
| ------------------------- | ----------------------------------------------- | ------------------------------------------------------- |
| **Agentic AI**            | `LangGraph`                                     | Orchestration of planner, evaluator, and monitor agents |
| **Data Retrieval (RAG)**  | `LlamaIndex`, `ChromaDB`                        | Contextual data for planning from mission archives      |
| **Machine Learning**      | `Scikit-learn`, `PyTorch` (TCN)                 | Anomaly detection on trajectory data                    |
| **Orbital Simulation**    | `GMAT` (General Mission Analysis Tool)          | High-fidelity trajectory generation & simulation        |
| **Visualization**         | `Streamlit`, `Plotly`                           | Interactive mission control dashboard                   |
| **API & Backend**         | `FastAPI`                                       | Service layer for agent and simulation interaction      |
| **Observability**         | `LangSmith`                                     | Debugging and tracing agent decisions                   |

## 🏁 Project Roadmap

This project is structured into distinct phases, each delivering a key capability and building towards the final system.

-   [X] **Phase 0: Setup & Scaffolding**
    -   *Outcome*: Project structure, virtual environment, and all dependencies are in place.

-   [ ] **Phase 1: Baseline Trajectory Simulation (Weeks 1-2)**
    -   *Goal*: Simulate and visualize a baseline Earth-to-Mars Hohmann transfer using GMAT.
    -   *Key Tools*: GMAT, Python, Streamlit.
    -   *Outcome*: A script that generates a valid trajectory and a simple dashboard to plot it.

-   [ ] **Phase 2: Agentic Architecture & Initial Decision Flow (Weeks 3-5)**
    -   *Goal*: Implement the core agentic loop (Planner, Evaluator) using LangGraph.
    -   *Key Tools*: LangGraph, LangSmith.
    -   *Outcome*: An agent that can propose a mission plan and have it validated based on simple rules.

-   [ ] **Phase 3: RAG Integration for Domain Intelligence (Weeks 6-7)**
    -   *Goal*: Enhance the Planner agent with a RAG pipeline to query historical mission data.
    -   *Key Tools*: LlamaIndex, ChromaDB.
    -   *Outcome*: The Planner can make more informed decisions based on external documents.

-   [ ] **Phase 4: Anomaly Detection & Reactive Replanning (Weeks 8-10)**
    -   *Goal*: Introduce an anomaly detection model and a replanning loop.
    -   *Key Tools*: Scikit-learn, LangGraph.
    -   *Outcome*: The system can detect simulated trajectory deviations and autonomously trigger a correction.

-   [ ] **Phase 5: Advanced Visualization & Explainability (Weeks 11-12)**
    -   *Goal*: Build out the Streamlit dashboard into a full mission control UI.
    -   *Outcome*: A dashboard showing the live trajectory, agent logs, anomaly alerts, and decision rationales.

-   [ ] **Phase 6: Final Polish & Documentation (Weeks 13-14)**
    -   *Goal*: Complete all documentation, create a final demo, and publish the project.
    -   *Outcome*: A polished, portfolio-ready project with a comprehensive README and presentation materials.

## 🚀 Advanced Extensions & Future Work

Beyond the core roadmap, AegisNav is designed to be extensible. The following advanced components can be integrated to further enhance its capabilities, typically after the core system is functional.

| Component                       | Technology / Concept         | Why It Would Be Added                                                                  |
| ------------------------------- | ---------------------------- | -------------------------------------------------------------------------------------- |
| **Advanced Anomaly Detection**  | `PyTorch` (TCNs/LSTMs)       | To move beyond baseline models and capture complex temporal patterns in telemetry data for more subtle anomaly detection. |
| **Domain-Specific AI Planner**  | `LoRA` Fine-Tuning           | To specialize the LLM planner on nuanced trajectory optimization tasks, improving its efficiency and accuracy for space-specific problems. |
| **Enhanced Safety Alignment**   | `RLHF`/`Constitutional AI`   | To enforce hard safety, ethical, and operational constraints on the agent's decisions, critical for mission-critical autonomy. |
| **High-Fidelity Simulation**    | `SPICE Toolkit` (NASA)       | To add precision spacecraft orientation, instrument timing, and ephemeris data for more realistic mission simulation. |
| **Explainable AI (XAI)**        | `SHAP`                       | To provide deep, quantitative insights into *why* the anomaly detection model flagged a specific deviation. |
| **3D Mission Visualization**    | `Unreal Engine`/`Omniverse`  | To create a visually stunning, high-fidelity digital twin of the mission, ideal for presentations and demonstrations. |

## ⚙️ Getting Started

### Prerequisites

-   Python 3.10+
-   GMAT (installed and configured)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/romandidomizio/space-autonomy.git
    cd space-autonomy
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```bash
    streamlit run ui/dashboard.py
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
