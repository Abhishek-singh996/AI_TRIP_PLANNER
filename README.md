<p align="center">
  <img src="git_readme_images/project_logo.png" width="280" />
</p>

<p align="center">
  <!-- Python Version -->
  <img src="https://img.shields.io/badge/Python-3.12-blue.svg" />

  <!-- License -->
  <img src="https://img.shields.io/badge/License-MIT-green.svg" />

  <!-- Build Status (GitHub Actions placeholder) -->
  <img src="https://img.shields.io/badge/Build-Passing-brightgreen.svg" />
</p>

# 🧠 AI Trip Planner

AI Trip Planner is an intelligent travel-planning system powered by LLM agents, custom tools, and workflow automation.  
It generates personalized itineraries, suggests destinations, checks weather conditions, converts currencies, and provides a complete AI-powered trip planning experience.

This project follows a clean, modular architecture using **Python**, **UV**, and reusable agents/tools.

---

## 🚀 Features

### 🗺️ Smart Itinerary Generation
- Multi-step reasoning using an AI agent workflow  
- Personalized trip planning: interests, duration, budget, weather, etc.  
- Multi-day itinerary output  

### 🔧 Custom Tooling
Located under `tools/`:
- Currency Conversion Tool  
- Weather Info Tool  
- Place Search Tool  
- Arithmetic Utility Tool  

### 📁 Configurable & Modular
- YAML-based configuration (`config/config.yaml`)  
- Reusable prompt templates (`prompt_library/`)  
- Utility layer for model loading, config loading, calculations, document creation, etc.

### 🧩 Extendable Agent Workflow
- Agent logic stored in `agent/agent_workflow.py`
- Allows adding/removing tools or custom steps easily

---

## 🏗️ System Architecture

Below is a high-level architecture diagram showing how the AI Trip Planner processes user inputs and interacts with tools:

<p align="center">
  <img src="git_readme_images/architecture.png" width="650" />
</p>

---

## 📁 Project Structure
```
AI_TRIP_PLANNER/
├── agent/ # Agent logic & workflow
├── app.py # Application entry point
├── main.py # Script for manual agent execution
├── tools/ # Custom AI tools
├── utils/ # Utility modules
├── config/ # YAML configuration
├── prompt_library/ # Prompt templates
├── notebook/ # Notebook experiments
├── requirements.txt # Dependencies (if not using uv)
├── pyproject.toml # Project metadata for UV
├── setup.py # Packaging configuration
└── README.md # Documentation
```



