# SOMARA DevSecOps Platform

A small end-to-end DevSecOps platform demonstrating secure application development, automated security testing, container security, CI/CD deployment, production monitoring, alerting, and automatic rollback.

---

## 📌 Project Overview

SOMARA DevSecOps Platform is a lightweight production-style application built with FastAPI and deployed on Daruur Space.

The project demonstrates how security can be integrated throughout the software development lifecycle:

```text

Code

  ↓

Test

  ↓

Security Scan

  ↓

Build

  ↓

Container Security

  ↓

Registry

  ↓

Deployment

  ↓

Health Check

  ↓

Rollback if Required

  ↓

DAST

  ↓

Monitoring

  ↓

Alerting



                           SOMARA DevSecOps

                                  |

                                  v

                         ┌─────────────────┐

                         │     Developer   │

                         └────────┬────────┘

                                  |

                                  v

                         ┌─────────────────┐

                         │     GitHub      │

                         │   Repository    │

                         └────────┬────────┘

                                  |

                                  v

                    ┌──────────────────────────┐

                    │     GitHub Actions       │

                    └────────────┬─────────────┘

                                 |

             ┌───────────────────┼───────────────────┐

             |                   |                   |

             v                   v                   v

        ┌─────────┐        ┌───────────┐       ┌──────────┐

        │ Semgrep │        │ pip-audit │       │ Gitleaks │

        │  SAST   │        │Dependency │       │ Secrets  │

        └────┬────┘        │   Scan    │       └────┬─────┘

             |             └─────┬─────┘            |

             |                   |                   |

             └───────────────────┼───────────────────┘

                                 |

                                 v

                         ┌─────────────────┐

                         │     Pytest      │

                         │ Automated Tests │

                         └────────┬────────┘

                                  |

                                  v

                         ┌─────────────────┐

                         │  Docker Build   │

                         └────────┬────────┘

                                  |

                                  v

                         ┌─────────────────┐

                         │     Trivy       │

                         │Container Scan   │

                         └────────┬────────┘

                                  |

                                  v

                         ┌─────────────────┐

                         │      GHCR       │

                         │Container Image  │

                         └────────┬────────┘

                                  |

                                  v

                    ┌──────────────────────────┐

                    │      Daruur Space        │

                    │       Ubuntu Server      │

                    └────────────┬─────────────┘

                                 |

                                 v

                         ┌─────────────────┐

                         │      Docker     │

                         │ SOMARA Backend  │

                         └────────┬────────┘

                                  |

                                  v

                         ┌─────────────────┐

                         │      Nginx      │

                         │ Reverse Proxy   │

                         └────────┬────────┘

                                  |

                                  v

                              HTTPS

                                  |

                                  v

                         ┌─────────────────┐

                         │     FastAPI     │

                         │      API        │

                         └────────┬────────┘

                                  |

                 ┌────────────────┼────────────────┐

                 |                |                |

                 v                v                v

          ┌────────────┐   ┌────────────┐   ┌────────────┐

          │ Prometheus │   │  Grafana   │   │ OWASP ZAP  │

          │ Monitoring │   │ Dashboards │   │    DAST    │

          └─────┬──────┘   └─────┬──────┘   └────────────┘

                |                |

                └───────┬────────┘

                        v

                 Email Alerting







                 # 🧰 Technology Stack

SOMARA DevSecOps Platform uses a lightweight, security-focused technology stack covering application development, containerization, CI/CD, security automation, cloud infrastructure, observability, and production operations.

---

## Application Layer

| Technology | Role | Purpose |

|---|---|---|

| **Python 3.12** | Programming Language | Backend application development |

| **FastAPI** | Web Framework | High-performance REST API |

| **Uvicorn** | ASGI Server | Production application server |

| **Pydantic** | Data Validation | Request and response validation |

| **Pytest** | Testing Framework | Automated unit and integration testing |

| **Prometheus FastAPI Instrumentator** | Observability | Application metrics instrumentation |

---

## Source Control & CI/CD

| Technology | Role | Purpose |

|---|---|---|

| **Git** | Version Control | Source code management |

| **GitHub** | Source Repository | Code hosting and collaboration |

| **GitHub Actions** | CI/CD Platform | Automated build, test, security scanning, and deployment |

| **GitHub Container Registry (GHCR)** | Container Registry | Secure Docker image storage and distribution |

---

## DevSecOps & Security

| Technology | Security Function | Purpose |

|---|---|---|

| **Semgrep** | SAST | Static application security testing |

| **pip-audit** | SCA | Python dependency vulnerability analysis |

| **Gitleaks** | Secret Scanning | Detection of exposed credentials and secrets |

| **Trivy** | Container Security | Docker image vulnerability scanning |

| **OWASP ZAP** | DAST | Dynamic application security testing |

| **Docker Security Controls** | Runtime Security | Container isolation and privilege reduction |

| **UFW** | Network Security | Host-based firewall management |

| **Let's Encrypt** | TLS Security | HTTPS certificate management |

---

## Containerization & Runtime

| Technology | Role | Purpose |

|---|---|---|

| **Docker** | Container Runtime | Application packaging and deployment |

| **Docker Engine** | Runtime Platform | Production container execution |

| **Python Slim Images** | Base Image | Reduced container footprint |

| **Non-root User** | Container Security | Prevent privileged application execution |

| **CAP_DROP=ALL** | Linux Security | Remove unnecessary Linux capabilities |

| **No New Privileges** | Runtime Security | Prevent privilege escalation |

| **Read-only Root Filesystem** | Runtime Security | Reduce filesystem modification |

| **Tmpfs `/tmp`** | Runtime Isolation | Controlled temporary writable storage |

| **CPU & Memory Limits** | Resource Governance | Prevent uncontrolled resource consumption |

---

## Cloud & Infrastructure

| Technology | Role | Purpose |

|---|---|---|

| **Daruur Space** | Cloud Infrastructure | Production hosting environment |

| **Ubuntu 24.04 LTS** | Operating System | Production server platform |

| **Nginx** | Reverse Proxy | HTTPS termination and traffic forwarding |

| **UFW** | Host Firewall | Restrict inbound network access |

| **Let's Encrypt** | Certificate Authority | Automated TLS certificates |

---

## Observability & Monitoring

| Technology | Role | Purpose |

|---|---|---|

| **Prometheus** | Metrics Collection | Collect application and infrastructure metrics |

| **Node Exporter** | Infrastructure Metrics | Export Linux server metrics |

| **Grafana** | Visualization | Monitoring dashboards and observability |

| **Grafana Alerting** | Alert Management | Detect operational conditions |

| **Email Notifications** | Notification Channel | Deliver production alerts |

---

## Deployment & Reliability

| Technology / Mechanism | Purpose |

|---|---|

| **GitHub Actions** | Automated deployment |

| **SSH Deployment** | Secure remote deployment |

| **Docker Image Tags** | Release traceability |

| **Health Checks** | Deployment validation |

| **Automatic Rollback** | Recovery from failed deployments |

| **Nginx Reverse Proxy** | Controlled production traffic |

| **HTTPS** | Encrypted client-to-server communication |

---

## Security Architecture

The technology stack implements security controls across the complete software delivery lifecycle:

```text

┌─────────────────────────────────────────────────────────────┐

│                    SOMARA DevSecOps                        │

├─────────────────────────────────────────────────────────────┤

│                                                             │

│  SOURCE CODE                                                │

│      │                                                      │

│      ├── Git / GitHub                                       │

│      │                                                      │

│      ▼                                                      │

│  CODE SECURITY                                               │

│      ├── Semgrep          → SAST                            │

│      ├── Gitleaks         → Secret Scanning                 │

│      └── pip-audit        → Dependency Security             │

│      │                                                      │

│      ▼                                                      │

│  QUALITY                                                    │

│      └── Pytest            → Automated Testing              │

│      │                                                      │

│      ▼                                                      │

│  CONTAINER SECURITY                                          │

│      ├── Docker            → Containerization               │

│      └── Trivy             → Vulnerability Scanning         │

│      │                                                      │

│      ▼                                                      │

│  REGISTRY                                                    │

│      └── GHCR              → Image Storage                   │

│      │                                                      │

│      ▼                                                      │

│  PRODUCTION                                                  │

│      ├── Daruur Space      → Cloud Infrastructure            │

│      ├── Ubuntu            → Operating System                │

│      ├── Docker            → Runtime                         │

│      └── Nginx             → Reverse Proxy                   │

│      │                                                      │

│      ▼                                                      │

│  RUNTIME SECURITY                                            │

│      ├── Non-root User                                      │

│      ├── CAP_DROP=ALL                                       │

│      ├── No New Privileges                                  │

│      ├── Read-only Filesystem                               │

│      ├── Restricted /tmp                                    │

│      └── CPU / Memory Limits                                │

│      │                                                      │

│      ▼                                                      │

│  VALIDATION                                                  │

│      ├── Health Check                                       │

│      ├── OWASP ZAP         → DAST                           │

│      └── Automatic Rollback                                  │

│      │                                                      │

│      ▼                                                      │

│  OBSERVABILITY                                               │

│      ├── Prometheus        → Metrics                        │

│      ├── Node Exporter     → Server Metrics                 │

│      ├── Grafana           → Dashboards                      │

│      └── Email Alerts      → Notifications                   │

│                                                             │

└─────────────────────────────────────────────────────────────┘



Application

├── Python

├── FastAPI

├── Uvicorn

├── Pydantic

└── Pytest

DevSecOps

├── Git

├── GitHub

├── GitHub Actions

├── Semgrep

├── pip-audit

├── Gitleaks

├── Trivy

└── OWASP ZAP

Containerization

├── Docker

├── GHCR

├── Non-root Containers

├── Linux Capabilities

├── Read-only Filesystem

└── Resource Limits

Infrastructure

├── Daruur Space

├── Ubuntu 24.04 LTS

├── Nginx

├── UFW

└── Let's Encrypt

Observability

├── Prometheus

├── Node Exporter

├── Grafana

└── Email Alerting

📁 Project Structure

The SOMARA DevSecOps Platform follows a simple and maintainable repository structure that separates application code, automated tests, container configuration, and CI/CD automation.

SOMARA-Devsecops-platform/
│
├── .github/
│   └── workflows/
│       └── devsecops.yml
│
├── app/
│   └── backend/
│       ├── main.py
│       ├── test_main.py
│       ├── requirements.txt
│       └── Dockerfile
│
└── README.md

Directory and File Overview

Path

Type

Description

.github/

Directory

GitHub repository configuration and automation

.github/workflows/

Directory

GitHub Actions workflow definitions

.github/workflows/devsecops.yml

Workflow

Complete CI/CD and DevSecOps pipeline

app/

Directory

Application source code

app/backend/

Directory

FastAPI backend service

app/backend/main.py

Python

FastAPI application and API endpoints

app/backend/test_main.py

Python

Automated application and security-header tests

app/backend/requirements.txt

Text

Python application and testing dependencies

app/backend/Dockerfile

Dockerfile

Secure container image build definition

README.md

Markdown

Project documentation and technical reference

Backend Components

The backend contains the core FastAPI application, its automated tests, dependency definitions, and Docker build configuration.

app/backend/
│
├── main.py
│   └── FastAPI application
│
├── test_main.py
│   └── Automated tests
│
├── requirements.txt
│   └── Python dependencies
│
└── Dockerfile
    └── Container image definition

CI/CD Components

The GitHub Actions workflow is responsible for the automated DevSecOps lifecycle:

.github/workflows/devsecops.yml
│
├── SAST
│   └── Semgrep
│
├── Dependency Security
│   └── pip-audit
│
├── Secret Security
│   └── Gitleaks
│
├── Automated Testing
│   └── Pytest
│
├── Container Security
│   └── Docker + Trivy
│
├── Container Registry
│   └── GitHub Container Registry
│
├── Production Deployment
│   └── Daruur Space
│
├── Deployment Validation
│   └── Health Check
│
├── Recovery
│   └── Automatic Rollback
│
└── DAST
    └── OWASP ZAP

This structure keeps the project lightweight while providing clear separation between application development, testing, security automation, containerization, deployment, and documentation