# Multi-Agent System Fault Injection and Fault Tolerance Evaluation Project

## Project Overview

This project is a systematic research effort focused on **fault injection, fault classification, and fault tolerance analysis in multi-agent systems**. Through structured fault injection testing of multi-agent systems driven by different LLM models, we evaluate their robustness and fault tolerance capabilities when encountering various types of faults.

## Core Research Objectives

1. **Systematic Fault Injection**: Design and implement fault injection methods for multi-agent systems
2. **Fault Classification Framework**: Establish a comprehensive fault type classification framework
3. **Fault Tolerance Evaluation**: Assess multi-agent system responses and recovery capabilities under various fault scenarios
4. **Model Comparison Analysis**: Compare performance differences among different LLM models (DeepSeek-v3, GPT-5, etc.)

## Project Structure

```
data/
├── data/                           # Main data directory
│   ├── Camel/                      # CAMEL multi-agent framework test results
│   │   ├── deepseek-v3/            # DeepSeek v3 model results
│   │   │   ├── baseline/           # Baseline tests (without fault injection)
│   │   │   └── injection/          # Fault injection tests
│   │   └── gpt-5/                  # GPT-5 model results
│   │       ├── baseline/
│   │       └── injection/
│   │
│   ├── Metagpt/                    # MetaGPT multi-agent framework test results
│   │   ├── deepseek-v3/
│   │   │   ├── baseline/
│   │   │   └── injection/
│   │   └── gpt-5/
│   │       ├── baseline/
│   │       └── injection/
│   │
│   ├── Table-Critic/               # Table-Critic framework test results
│   │   ├── deepseek-v3/
│   │   │   ├── baseline/
│   │   │   └── injection/
│   │   └── gpt-5/
│   │       ├── baseline/
│   │       └── injection/
│   │
│   ├── camel.csv                   # CAMEL framework test results 
│   ├── metagpt.csv                 # MetaGPT framework test results 
│   ├── tablecritic.csv             # Table-Critic framework test results summary
│   └── tag.csv                     # Fault labels and fault tolerance mechanism classification 

```

## Key Datasets

### 1. Testing Frameworks

| Framework | Description |
|-----------|-------------|
| **CAMEL** | Multi-agent collaboration framework supporting agent-to-agent communication | 
| **MetaGPT** | Large-scale multi-agent framework supporting complex workflows | 
| **Table-Critic** | Table processing and validation framework 

### 2. LLM Models

- **DeepSeek-v3**: An efficient open-source model
- **GPT-5**: The most advanced commercial language model

### 3. Test Modes

- **Baseline**: Fundamental tests without fault injection to assess normal system performance
- **Injection**: Tests with fault injection to evaluate system fault tolerance capabilities

## Benchmark Testing

### Benchmark Overview

The project uses three standard task sets from different domains to assess the performance and fault tolerance capabilities of multi-agent systems, covering three critical application areas: code generation, table question answering, and web interaction.

### 1. MetaGPT - HumanEval (Code Generation)

**Framework Characteristics**: Large-scale multi-agent system
- Number of agents: Dynamically determined (2-4 agents) based on task difficulty
- Application domain: Code generation

**Task Description**:
- Code generation tasks similar to competitive programming problems
- Examples: Determine if the difference between any two numbers in a list is less than a threshold, compute GCD, find shortest palindrome substring, etc.
- **Total tasks**: 164

**Baseline Performance (Without Fault Injection)**:

| Model | Success Rate | Sample Count |
|-------|--------------|--------------|
| **GPT-5** | 99% | 161 |
| **DeepSeek-v3** | 89% | 146 |



### 2. Table-Critic - WikiTQ (Table Question Answering)

**Framework Characteristics**: Medium-scale multi-agent system
- Number of agents: Fixed 5-agent workflow
- Application domain: Table QA and data analysis

**Task Description**:
- Given relevant tables and questions, the model must provide answers
- Example: How many people were murdered in 1940-1941?
- **Total tasks**: 400 (from test set; original dataset split: 11,321 training + 2,831 validation + 4,344 test)

**Baseline Performance (Without Fault Injection)**:

| Model | Success Rate | Sample Count |
|-------|--------------|--------------|
| **GPT-5** | 87% | 348 |
| **DeepSeek-v3** | 78.25% | 313 |

### 3. CAMEL - WebShop (Web Shopping)

**Framework Characteristics**: Simple-scale multi-agent system
- Number of agents: 2 agents
- Application domain: Web environment interaction and shopping decisions

**Task Description**:
- Given normalized, text-based web shopping environment and shopping instructions
- Agents need to browse pages, view details, select product attributes, and click purchase buttons
- Example: Find me a machine-washable men's long-sleeve t-shirt in dark brown, size 5XL, under $50
- **Total tasks**: 251 (annotated and difficulty-classified by AgentBoard)

**Baseline Performance (Without Fault Injection)**:

| Model | Success Rate | Sample Count |
|-------|--------------|--------------|
| **GPT-5** | 37.8% | 95 |
| **DeepSeek-v3** | 33.0% | 83 |

**Benchmark Design Characteristics**:
1. **Multi-domain Coverage**: Code generation, data analysis, web interaction
2. **Model Scale Variance**: From simple 2-agent to complex dynamic 4-agent systems
3. **Difficulty Hierarchy**: Covers Simple, Easy, Medium, Hard difficulty levels
4. **Standardized Tasks**: Uses industry-recognized benchmark sets (HumanEval, WikiTQ, WebShop)
5. **Comprehensive Evaluation**: Assesses both baseline performance and fault tolerance under injection

## Fault Classification Framework

### Fault Classification System Documentation

![Fault Taxonomy](images/fault_taxonomy.png)



## Fault Tolerance Mechanism Evaluation

The project assesses system fault tolerance capabilities across four distinct dimensions:

### Fault Tolerance Dimensions

1. **Mechanism-Level FT**
   - Fault tolerance derived from the system's structural design and temporal redundancy mechanisms
   - Includes architectural features such as iterative critique loops, multi-agent voting schemes, and redundant execution paths
   - These mechanisms operate independently of agent reasoning and are embedded in the MAS coordination infrastructure

2. **Rule-Based FT**
   - Fault tolerance emerging from explicit procedural logic and heuristic rules encoded in the MAS implementation
   - Includes automatically deduplicates redundant messages and other deterministic behaviors
   - Activates when predefined conditions are met, regardless of the underlying model's reasoning capabilities

3. **Prompt-Level FT**
   - Rooted in the semantic robustness of user prompts
   - Leverages prompt engineering to guide agents through edge cases, clarify ambiguities, and maintain role boundaries
   - Pre-empts and mitigates faults through careful prompt design

4. **Reasoning-Level FT**
   - Driven by the agent's high-level cognitive reflection
   - Relies on the underlying model's semantic understanding to autonomously detect logical inconsistencies
   - Infers missing context and resolves conflicts through multi-agent debate and consensus-building

### Tolerance Results

- **Success**: The system can effectively handle faults
- **Failure**: The system cannot handle faults, resulting in task failure

## Dataset Details

### camel.csv
- **Fields**: Test System, Base Model, Failure Type, Task ID, Agent Behavior Category, Task Result
- **Record Count**: 1,603
- **Model Coverage**: deepseek-v3, gpt-5
- **Fault Types**: Blind Trust and multiple other types
- **Task Results**: PASS/FAIL

### metagpt.csv
- **Fields**: Similar to camel.csv
- **Record Count**: 4,606
- **Characteristics**: Comprehensive test results for MetaGPT framework

### tablecritic.csv
- **Fields**: Similar to camel.csv
- **Record Count**: 5,289
- **Characteristics**: Comprehensive test results for Table-Critic framework

### tag.csv
- **Fields**: Fault Category, Agent Behavior, Fault Tolerance Summary
- **Record Count**: 72
- **Characteristics**: Provides mapping relationships between fault classification and tolerance mechanisms
- **Purpose**: Maps each fault type and agent behavior to specific fault tolerance dimensions


#### Tolerance Dimension Summary

- **Prompt-level FT**: Success when proper prompting prevents fault manifestation
- **Logical-level FT**: Success when system-level filtering and validation catch faults
- **Mechanism-level FT**: Success when architectural features provide redundancy and recovery
- **Reasoning-level FT**: Success when agents use semantic understanding to detect and resolve faults

**Fault Classifications**:
  - Role Ambiguity
  - Instruction Ambiguity
  - Instruction Logic Conflict
  - Blind Trust
  - Critical Information Loss
  - Hallucination
  - Parameter Filling Error
  - Tool Format Error
  - Tool Selection Error
  - Message Cycle
  - Message Storm
  - Message Broadcast Amplification
  - Memory Loss
  - Context Length Violation
  - Inexecutable Plan

## Fault Injection Methods

### Detailed Fault Injection Methods Documentation

![Fault Injection Methods](images/all_fault_injection.png)



1. **Prompt Modification**
   - Introduce ambiguities in system prompts
   - Add contradictory instructions
   - Hide critical information

2. **Input Contamination**
   - Mix incorrect information in inputs
   - Modify parameter values
   - Remove critical data

3. **Intermediate Process Interference**
   - Intercept agent-to-agent communication
   - Modify message content
   - Simulate faulty responses


### Injection Dimensions

The project injects faults across multiple dimensions to comprehensively evaluate fault tolerance:

1. **Fault Type Dimension**: Role ambiguity, instruction ambiguity, hallucination, blind trust, etc.
2. **Tolerance Level Dimension**: Mechanism-level, rule-based, prompt-level, reasoning-level tolerance
3. **Framework Dimension**: Different multi-agent frameworks (CAMEL, MetaGPT, Table-Critic)
4. **Model Dimension**: Different LLM models (DeepSeek-v3, GPT-5)



## Key Findings and Applications

### Research Outcomes

1. **Model Difference Analysis**
   - Different LLMs show varying sensitivity to faults
   - Relative advantages in fault tolerance capabilities

2. **Framework Comparison**
   - Design characteristics of various multi-agent frameworks
   - Effectiveness of built-in tolerance mechanisms

3. **Fault Pattern Recognition**
   - Identification of common agent failure patterns
   - Correlation among fault types

### Application Value

- **System Design**: Guide robust design of multi-agent systems
- **Model Evaluation**: Provide references for LLM selection
- **Tolerance Optimization**: Improve system fault handling capabilities
- **Risk Assessment**: Identify potential risks in production environments


