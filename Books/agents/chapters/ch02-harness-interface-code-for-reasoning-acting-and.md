---
source_pdf: "all.pdf"
chapter_number: 2
title: "Harness Interface: Code for Reasoning, Acting, and Environment Modeling"
source_page_start: 6
source_page_end: 14
---

# Chapter 2: Harness Interface: Code for Reasoning, Acting, and Environment Modeling

A harness turns a stateless language model into a functional agent by grounding its outputs in external
execution, persistent state, and verifiable feedback. The most fundamental design question for any harness is
therefore: _what medium connects the model to its task environment?_


We argue that code is the answer. Unlike natural language, code is _executable_, meaning model outputs
become operations with formally verifiable outcomes; _inspectable_, meaning intermediate computation is
exposed as structured traces that the harness can read, store, and act upon; and _stateful_, meaning the
evolving program represents task progress in a persistent, modifiable form across steps. Crucially, these
are not merely properties of code as a notation; they are properties that make code functional as a harness
interface. Executability means the harness can verify what the model intended. Inspectability means failures
can be diagnosed and fed back. Statefulness means the agent’s interaction history is not lost between steps.


**Scope boundary.** We use _code_ broadly, but not metaphorically. In this survey, code refers to executable or
machine-checkable artifacts, including programs, scripts, formal specifications, proof scripts, API schemas,
tool definitions, tests, repositories, simulators, configuration files, and code-adjacent execution artifacts
such as traces and logs when they are produced by or consumed by executable systems. By contrast, raw
perception, physical state, human intent, and model-internal latent reasoning are not themselves code.
They may be sensed, estimated, serialized, verified, or acted upon through code, but they should not be
conflated with the code interface. This boundary is important because code as a harness interface does not
replace perception, embodiment, human goals, or model reasoning; rather, it makes selected aspects of them
executable, inspectable, and stateful within the agent loop.


We organize this interface around three roles that code assumes in agentic systems. _Code_ _for_ _reasoning_
externalizes internal logic into verifiable computation, allowing external interpreters, symbolic solvers,
execution traces, or process rewards to check and refine reasoning (§2.1). _Code for acting_ translates highlevel intent into executable operations grounded in embodied, GUI, software, or tool-use environments (§2.2).
_Code for environment modeling_ represents world state, transition dynamics, and feedback signals through
program states, repositories, simulators, tests, and logs that agents can execute, edit, and query (§2.3).
Overall, these roles define the harness interface: code makes reasoning executable, action programmable,
and environment state inspectable.


**2.1.** **Code for Reasoning**


A central role of the agent harness is to transform model reasoning from transient text generation into
executable and verifiable computation. Early prompting techniques such as pure chain-of-thought (CoT) [65]
perform reasoning and computation entirely in _natural_ _language_, forcing the model to both decompose
problems and execute intermediate operations within a single latent textual process. While language models
are often effective at proposing reasoning steps, they remain unreliable at faithfully carrying out symbolic,
logical, or arithmetic computation [7]. More importantly, purely textual reasoning provides the agent harness
with little ability to verify intermediate states, inspect execution behavior, or persist computational progress
across steps.


_Code-for-reasoning_ thus introduces code as the execution interface between the model and the harness, moving
beyond purely text-based reasoning. The model generates executable programs that external runtimes,
interpreters, symbolic solvers, or verification modules can execute and evaluate. This separates high-level
reasoning from low-level computation: the model proposes procedures, while the harness executes them,


<!-- source-page: 6 -->


**Code helps the agent reason.**


**Code translates intent into action.**


**Code makes env. inspectable and traceable.**


**Figure** 2: Overview of code as the harness interface, connecting agents to reasoning, action, and
environment modeling through executable programs, tool calls, state tracking, and feedback traces.


observes runtime behavior, stores intermediate states, and feeds execution results into future reasoning.


Recent work further broadens this interface from program execution as an external calculator to execution
artifacts as reusable reasoning signals. Inputs and outputs, execution traces, variable states, control-flow
structures, and function-level tests can all serve as intermediate states that the harness verifies, scores,
and feeds back into subsequent reasoning. Existing work can therefore be organized into three paradigms:
program-delegated reasoning, formal verification and symbolic reasoning, and iterative code-grounded
reasoning. We detail each of them in the following subsections.


_**2.1.1.**_ _**Program-Delegated Reasoning**_


Program-delegated reasoning uses executable programs as the primary interface between problem decomposition and computation. Instead of relying solely on natural language reasoning, the model generates code
that external interpreters execute to produce formally grounded outputs. Early works [66, 7] demonstrate
that delegating computation to programs substantially improves reliability by moving intermediate reasoning
into structured, verifiable execution traces. Program-of-Thoughts (PoT) prompting [6] further systematizes
this paradigm by explicitly decomposing reasoning into executable programs, followed by extensions such as
POET [67] and MathCoder [68], which improve execution fidelity and domain specialization. Subsequent
work investigates the conditions under which program delegation is effective, including the role of execution
correctness, task structure, and runtime interaction. For example, Chain of Code (CoC) [8] and CIRS [69]
analyze how executable reasoning changes failure modes relative to pure language-based reasoning. Later
directions extend this interface beyond isolated task execution. Cross-lingual reasoning frameworks [70]
demonstrate that program-based reasoning can generalize across linguistic environments through shared
executable structure, while method-based reasoning [71] introduces reusable programmatic procedures
that persist across tasks. More recent systems such as CodeAdapt [72] further suggest that tightly coupling
language models with executable reasoning interfaces can surpass specialized reasoning-oriented models.
Additionally, CodeI/O [73] transforms contextually grounded programs into code input-output prediction
tasks, exposing reasoning primitives such as logic-flow planning, state-space search, decision-tree traversal,
and modular decomposition while preserving procedural rigor through executable verification.


<!-- source-page: 7 -->


**Figure** 3: Roadmap of the harness interface, organized by code’s role in reasoning, acting, and environment
modeling, with representative works ordered chronologically within each role.


_**2.1.2.**_ _**Formal Verification and Symbolic Reasoning Interfaces**_


Hybrid neural-symbolic methods combine flexible language-based inference with structured symbolic computation, using code and symbolic artifacts as persistent intermediate representations rather than treating
programs as mere generated text. Early formulations such as Graph-of-Thoughts [74] generalize chain-ofthought reasoning into graph-structured trajectories, enabling intermediate states to branch, merge, and be
reused. Building on this direction, self-verifying reflection [75], MA-LoT [76], and Socratic self-refine [77]
introduce iterative verification loops in which symbolic consistency checks guide the refinement of generated
solution paths.


Recent work further tightens the coupling between neural generation and symbolic execution through
code-based interfaces. CodeSteer [78] and Code-as-Symbolic-Planner [79] explicitly coordinate free-form
language reasoning with executable symbolic operations, treating programs as structured substrates that the
harness can inspect, transform, and execute across multiple stages. VisualCoder [80] extends this idea by
making program behavior visible through control-flow representations. By aligning generated reasoning
with visual control-flow graphs and execution paths, it turns dynamic program behavior into an inspectable


<!-- source-page: 8 -->


artifact for program-behavior prediction. Together, these methods broaden the neural-symbolic interface
from textual code to multimodal execution artifacts that a harness can reference, validate, and reuse.


A complementary line of work uses machine-verifiable formal languages as the reasoning interface itself. Proof
assistants such as Lean [81], Isabelle [82], and Coq [83] provide formal proof languages based on rigorous
logical foundations, enabling each derivation step to be checked by a verifier. Early LLM-based theoremproving systems, including ReProver [84], DeepSeek-Prover [85], and TheoremLlama [86], establish practical
recipes for combining language models with proof-assistant feedback in mathematical reasoning. More recent
systems, such as DeepSeek-Prover-V2 [87], Kimina-Prover [88], MA-LoT [76], and Goedel-Prover-V2 [89],
improve this process through deliberative proof search, self-correction, and repeated proof generation and
verification. Formal verification interfaces are also expanding beyond theorem proving in mathematics.
HybridReasoning [90] applies formal provers to support natural-language reasoning; Lean4Physics [91]
and PhysLib [92] extend Lean-based verification to physics; and VERINA [93] and Goedel-Code-Prover [94]
adapt formal methods to code verification. Lean4Agent [95] further extends this trajectory to agentic systems
by using Lean4 to model and verify agent workflows and trajectories. From the harness perspective, these
systems show how formal languages can serve not only as reasoning tools, but also as executable contracts
that constrain, certify, and audit agent behavior.


_**2.1.3.**_ _**Iterative Code-Grounded Reasoning**_


Iterative code-grounded reasoning focuses on closed-loop interaction between generation, execution, and
feedback. In these systems, reasoning is not a single-pass process, but an iterative computational trajectory
grounded in executable state transitions. Early work such as NExT [30] trains models to anticipate execution
behavior by reasoning over program traces, thereby grounding intermediate reasoning in runtime semantics.
Related efforts [96] similarly emphasize that executable traces provide a richer supervision signal than
final textual outputs alone. Building on this foundation, subsequent approaches introduce explicit generate–
execute–verify–refine loops. Methods such as CodePRM [31] and ORPS [97] use execution outcomes to
evaluate and refine intermediate reasoning trajectories, enabling the harness to guide reasoning through
runtime feedback rather than pure next-token prediction. Along the same direction, systems such as
CYCLE [98] and Self-Edit [99] iteratively revise generated solutions using execution-aware correction signals.
Reinforcement learning further strengthens this paradigm by treating execution feedback as an optimization
signal over reasoning trajectories. Methods such as CodeRL [100], CodeRL+ [101], and RLTF [102]
optimize functional correctness through unit-test-based rewards, while approaches such as StepCoder [103]
incorporate fine-grained compiler and runtime feedback during optimization. RLEF [104] formalizes this
interaction as policy optimization grounded in multi-step execution feedback, allowing reasoning policies to
adapt through iterative runtime interaction. More recent approaches move toward fully interactive reasoning
environments. For example, EG-CFG [21] injects execution signals directly during generation to support
step-level correction, while systems such as R1-Code-Interpreter [105] interleave reasoning and multiple
rounds of code execution within persistent interactive sessions.


**2.2.** **Code for Acting**


Beyond reasoning, the agent must also connect the model to external environments where decisions produce
real executable effects. At this stage, code no longer serves primarily as a medium for computation, but as an
action interface that converts model outputs into grounded operations such as tool invocations, robot-control
policies, GUI actions, or software commands. Through this interface, the harness translates high-level
intent into executable behaviors that can interact with embodied, digital, and interactive environments. The


<!-- source-page: 9 -->


Table 1: Representative systems where code serves as a reasoning substrate.


**Method** **Mechanism** **Reasoning Paradigm** **Key Innovation**


PoT [6] Delegated Hybrid comments Merges code with natural language CoT
PAL [7] Delegated Program-aided Decouples logic from computation
CodeAdapt [72] Delegated Generalizable logic Code-enabled LLMs outperforming reasoning models
CodeI/O [73] Delegated I/O prediction Converts code into verifiable input-output reasoning tasks
SATLM [29] Formal SAT/SMT solving Uses symbolic solvers as machine-checkable reasoning backends
ReProver [84] Formal Lean proof search Combines LLM generation with proof-assistant feedback
Dpsk-Prover [85] Formal Lean theorem proving Trains LLMs for formal mathematical proof generation
Dpsk-Prover-V2 [87] Formal Deliberative proving Lean proof search through decomposition and self-correction
Goedel-Code- Formal Lean code proof Searches hierarchical Lean proofs for code verification
Prover [94]

Lean4Agent [95] Formal Agent verification Models and verifies agent workflows and trajectories in Lean4
Chain of Code [8] Hybrid LMulator Simulates non-executable semantic code
SATLM [29] Hybrid Formal Logic Uses SAT/SMT solvers as reasoning backend
CodeSteer [78] Hybrid Symbolic control Explicitly transitions between symbolic code and neural text
VisualCoder [80] Hybrid CFG-grounded Aligns code reasoning with visual control-flow artifacts.
NExT [30] Iterative Trace-grounded Anticipates execution behavior via program traces
MathCoder [68] Iterative Feedback-driven SFT Interleaves code, output, and reflection
CodePRM [31] Iterative Process rewards Learns reward functions over reasoning-execution trajectories
RLEF [104] Iterative Multi-step RL Optimizes policy directly using execution feedback
EG-CFG [21] Iterative Execution-guided Integrates execution signals directly during generation
R1-Code-Int. [105] Iterative Fully interactive Autonomously interleaves reasoning and multiple executions
ExecVerify [106] Iterative Stepwise RL Uses statement- and variable-level execution rewards.
FunPRM [107] Iterative Function-step PRM Treats functions as verifiable process-reward units.
ReCode [108] Iterative Process RL Reinforces code generation with reasoning-process rewards


central challenge is therefore grounding: the harness must map abstract language outputs into executable
behaviors that respect the constraints of the target environment, including embodiment limits, interface
APIs, environment dynamics, and safety requirements. Unlike code-for-reasoning, where interpreters can
often directly verify correctness, action execution occurs in partially observed and dynamically evolving
environments, where failures may emerge through invalid state transitions, delayed feedback, or silent
execution errors. For example, a robot may attempt to grasp an object outside its reachable workspace
without producing an explicit runtime exception.


Importantly, executable action code is an interface to these components, not a replacement for them. In
embodied settings, perception modules provide observations, affordance or feasibility models estimate which
actions are possible, motion planners and controllers connect symbolic commands to sensors and actuators,
and safety layers constrain dangerous or invalid behavior. In GUI and software settings, the analogous
components include screen parsers, DOM or accessibility trees, backend APIs, user-intent models, permission
systems, and programmatic validators. Code sits between the model and these components: it serializes
observations, calls grounding and planning modules, invokes executable actions, and exposes validation
results back to the harness.


_Code-for-acting_ therefore introduces structured executable programs as the control interface between the
model and the environment, allowing the harness to execute, monitor, validate, reuse, and refine actions
through interaction feedback. This interface can be realized in different forms: a predefined skill library, a


<!-- source-page: 10 -->


Table 2: Representative systems where code serves as an action interface.


**Method** **Mechanism** **Action Paradigm** **Key Innovation**


AutoHarness [109] Harness Action validation Synthesizes code harnesses that mediate model actions and filter
Gen. invalid environment interactions
SayCan [9] Skill Selec. Affordance-based Links LLM plans to physical feasibility
KnowNo [110] Skill Selec. Conformal prediction Calibrates planner uncertainty for ambiguous instructions
SkillVLA [111] Skill Selec. Bimanual grounding Extends grounding to combinatorial skill reuse
BOSS [112] Skill Selec. Skill bootstrapping Synthesizes new executable skill chains via guided practice
LLM-Guided Skill Selec. Trajectory generation Generates diverse manipulation trajectories and executable success
Traj. [113] conditions
LRLL [114] Skill Selec. Lifelong grounding Evolving skill interface via memory and self-exploration
CaP [10] Policy Gen. Hierarchical Python Generates reactive robot control policies
RoboCodeX [33] Policy Gen. Multimodal tree Synthesizes tree-structured code across navigation
Code-BT [34] Policy Gen. Behavior-tree Imposes rule constraints via code-to-behavior-tree planning
ALRM [115] Policy Gen. Closed-loop control Integrates programmatic generation with ReAct execution
CP-Agent [116] Policy Gen. Constraint solving Uses persistent execution loops for formal constraint-model repair
Robot-Code Policy Gen. Static simulation Uses LLMs as static simulators for robot code evaluation
Sim. [117]

GenSwarm [118] Policy Gen. Multi-robot control Coordinates policy generation and deployment across robotic agents
NormCode [119] Policy Gen. Governed interface Enforces auditability and data isolation through semi-formal code
RACAS [120] Policy Gen. Cooperative control Robot-agnostic architecture for closed-loop cooperative agents
Voyager [32] Lifelong Skill Library Autonomous curriculum for open-ended tasks
LYRA [121] Lifelong Human-in-loop Encodes human corrections into reusable structured skills
ViReSkill [122] Lifelong Vision-grounded Replanning on failure using a skill-memory cache
UI-Voyager [35] Lifelong Self-evolving Rejection fine-tuning and self-distillation for mobile GUI agents
SkillsCrafter [123] Lifelong Continual skills Mitigates forgetting as executable manipulation skills accumulate


generated control policy, a persistent skill memory, a GUI/API tool protocol, or an explicit action-validation
harness. AutoHarness [109] makes the last form explicit by automatically synthesizing a code harness that
mediates between the LLM and the environment, filtering invalid actions before execution. This highlights
the core harness view of code-for-acting: code is not only the action to be executed, but also the executable
boundary that connects model intent to perception, grounding, affordance estimates, controllers, APIs,
actuators, and safety constraints.


_**2.2.1.**_ _**Grounded Skill Selection**_


Grounded skill selection studies how the agent maps high-level language intent into executable behaviors
through reusable skill interfaces. Rather than generating low-level actions directly, these systems treat the
environment as a collection of executable capabilities that the agent harness can invoke, compose, and refine
under environmental constraints. SayCan [9] establishes the core paradigm by coupling language planning
with grounded skill execution, allowing the agent to select actions based not only on semantic relevance
but also embodiment feasibility. Subsequent work extends this execution interface in several directions.
KnowNo [110] introduces uncertainty-aware control through conformal prediction, enabling the harness
to detect ambiguous states and trigger clarification before unsafe execution. BOSS [112] addresses the
rigidity of fixed skill libraries by using language-guided practice to synthesize new executable skill chains,
allowing the harness to expand its action space over time. Similarly, [113] tackles the data bottleneck
of grounded interaction by using LLM-guided generation to construct diverse manipulation trajectories


<!-- source-page: 11 -->


and executable success conditions for automatic retry and relabeling. Beyond static execution, LRLL [114]
introduces memory and self-guided exploration to maintain a persistent and evolving skill interface across
tasks. Finally, SkillVLA [111] extends this paradigm to combinatorial bimanual interaction, emphasizing
that grounded action interfaces must support structured skill reuse and recomposition under increasingly
complex embodiment settings.


_**2.2.2.**_ _**Programmatic Policy Generation**_


Programmatic policy generation treats code itself as the control interface between the model and the
environment. Instead of selecting from predefined skills, the harness directly materializes executable policies
as programs that specify control logic, perception-conditioned branching, feedback loops, and API interaction.
CaP [10] crystallizes this paradigm by framing LLM-generated Python programs as executable robot policies.
Building on this idea, RoboCodeX [33] introduces multimodal and tree-structured code generation to support
more complex manipulation and navigation behaviors. Subsequent work focuses on scaling the interaction
substrate. RoboPro [124] synthesizes executable policy code from large-scale in-the-wild videos, while CodeBT [34] compiles generated programs into behavior-tree controllers that support constrained execution and
iterative runtime feedback. Beyond robotics, CP-Agent [116] demonstrates that persistent execution loops
can support formal constraint-solving agents through iterative execution and repair. To reduce dependence
on expensive physical environments, [117] configures language models as static execution simulators for
robot code evaluation. GenSwarm [118] further extends programmatic control to multi-agent robotic
systems, where the harness must coordinate policy generation, constraint analysis, and deployment across
multiple embodied agents. At the systems level, NormCode [119] emphasizes governance and auditability by
introducing a semi-formal programming interface with enforced data isolation, allowing execution traces and
control logic to remain inspectable and constrained. Finally, ALRM [115] and RACAS [120] consolidate these
ideas into persistent closed-loop control architectures that integrate code generation, execution, monitoring,
and iterative interaction within unified agent harnesses.


_**2.2.3.**_ _**Lifelong Code-Based Agents**_


Lifelong code-based agents study how executable interaction interfaces can persist, evolve, and accumulate
capabilities over long-horizon interaction. In these systems, code is not only an execution mechanism, but
also a persistent memory substrate through which the harness stores reusable behaviors, interaction traces,
and environment knowledge. Voyager [32] establishes this paradigm through an automatic curriculum and
continually expanding executable skill library for open-ended interaction in Minecraft. Extending this idea
to embodied environments, LRLL [114] introduces persistent memory, self-guided task exploration, and
skill abstraction to overcome the limitations of fixed policy libraries without requiring gradient updates. A
central challenge in lifelong harnesses is that interaction feedback and corrections are often transient and
difficult to reuse. LYRA [121] addresses this issue by converting human corrections into reusable executable
skills and retrieval-augmented memory structures. Similarly, ViReSkill [122] combines vision-grounded
replanning with skill-memory caching to maintain stable interaction under environmental failures and
output variability. Recent work further focuses on continual adaptation and self-evolution under persistent
deployment. SkillsCrafter [123] introduces continual language-conditioned manipulation structures to
mitigate catastrophic forgetting as executable capabilities accumulate, while UI-Voyager [35] generalizes
the self-evolving interaction paradigm to GUI agents through failure-driven adaptation and self-distillation.
Together, these systems move beyond one-shot execution toward persistent agent harnesses that continuously
expand, refine, and reuse executable interaction interfaces over time.


<!-- source-page: 12 -->


Table 3: Representative systems where code serves as an environment representation.


**Method** **Mechanism** **Environment** **Key Innovation**

**Paradigm**


ViStruct [125] Structured Class/object hierarchy Encodes visual scenes as data structures
FactoredScenes [126] Structured Room programs Composes object/relation functions for 3D layout generation
PoE-World [127] Structured Programmatic experts Scales symbolic world models beyond simple grid-worlds
Code2World [38] Structured Render-aware RL Re-frames GUI state prediction as renderable HTML generation
SemCoder [128] Trace-based Semantic alignment Pairs code with detailed execution traces
WorldCoder [36] Trace-based Model-based RL Synthesizes transition and reward models
CWM [37] Trace-based Open-weights trace Trains large LLMs natively on program execution traces
RWML [129] Trace-based Self-supervised RL Aligns simulated next states with realized environment states
AWM [130] Trace-based World-modeling Aligns multiple executable world models across tasks
WorldMind [131] Trace-based Model fusion Coordinates executable world models from knowledge sources
SWE-bench [5] Evaluation Repo-level testing Uses unit tests as objective world states
AgentBench [12] Evaluation Multi-env interaction Benchmarks across OS, databases, and games
CRUXEval [132] Evaluation Execution tasks Benchmarks functional input and output prediction
End Terms. [39] Evaluation Procedural RL envs Automates generation of terminal-use evaluation tasks
InterCode [11] Evaluation Interactive execution Frames coding tasks as actions with sandbox feedback
LiveCodeBench [133] Evaluation Live coding eval Continuously updates execution-based evaluation pipelines
CRUXEval-X [134] Evaluation Multilingual execution Extends input-output execution evaluation across languages
CoRe [135] Evaluation Runtime reasoning Evaluates code reasoning through execution-centered tasks
CodeGlance [136] Evaluation Multimodal code eval Evaluates code understanding under visual and structural settings
SWE-smith [137] Construction Synthetic SWE envs Generates repository-level tasks and execution environments
EnvScaler [138] Construction Tool-interactive envs Synthesizes tool-use environments with programmatic validators


**2.3.** **Code for Environment**


The agent must also maintain an explicit representation of the environment with which the agent interacts.
Without such a representation, the environment is exposed to the agent only indirectly through textual
observations, API returns, or sparse feedback signals. As a result, environment state often remains implicit,
transient, and difficult to verify, making it challenging to track state transitions, evaluate interaction outcomes,
or reuse past interaction history across long-horizon tasks. This limitation becomes particularly severe in
complex software, robotic, and multi-step interactive environments, where successful interaction depends
on maintaining consistent world state and grounded feedback over time.


_Code-for-environment_ addresses this limitation by introducing executable programs as the environment
interface itself. Instead of treating the environment as an opaque external process, these systems materialize
environment structure and dynamics through computational artifacts such as simulators, repositories, tests,
execution traces, logs, and state-transition programs. This allows the agent to explicitly store, inspect, execute,
and modify environment state throughout interaction. Representing environments through executable code
provides two major advantages. First, executable environments expose verifiable state transitions, allowing
the agent to evaluate interaction outcomes through execution rather than ambiguous natural-language
judgment. Second, code-based environments are persistent and modifiable that agents can query, simulate,
edit, and refine during interaction. Rather than interacting with an opaque world solely through language,
agent harness can ground reasoning and action in explicit computational state and runtime dynamics. Existing
work in this direction can be organized into four paradigms: structured world representations, execution-trace
world modeling, code-grounded evaluation environments, and verifiable environment construction.


<!-- source-page: 13 -->


_**2.3.1.**_ _**Structured World Representations**_


Structured world representations model environments through explicit programmatic structures that the
agent can execute, inspect, and manipulate. Rather than representing the environment solely through
latent embeddings or textual descriptions, these approaches encode world state, object relations, spatial
layouts, and interaction dynamics as structured computational artifacts. For example, ViStruct [125] uses
programming-language structure as an explicit interface for visual structural knowledge extraction, enabling
multi-granular visual events to be represented through consistent executable structures. FactoredScenes [126]
similarly models indoor environments as compositional “room programs,” where reusable object and relation
functions define physically consistent scene layouts. Extending this idea to scalable symbolic world modeling,
PoE-World [127] introduces a compositional framework that combines many small programmatic experts to
represent increasingly complex environment dynamics. More recent systems broaden structured environment
interfaces to high-fidelity interactive worlds. Code2World [38] reframes GUI state prediction as renderable
HTML generation, allowing environment transitions to be represented and evaluated through executable
rendering code. Code2Worlds [139] further extends this paradigm to 4D simulated environments through
language-to-simulation program generation, where physics-aware execution loops reduce semantic-physical
inconsistencies during environment construction and interaction.


_**2.3.2.**_ _**Execution-Trace World Modeling**_


Execution-trace world modeling studies how the agent can learn environment dynamics directly from
executable interaction traces. Instead of treating execution merely as a final evaluation step, these approaches model runtime transitions themselves as the primary representation of environment behavior.
SemCoder [128] bridges static programs and runtime semantics by training language models to reason
about functional behavior, statement-level execution effects, and input-output transitions. Building on this
perspective, Code World Model (CWM) [37] learns predictive world models directly from program traces,
enabling the agent to anticipate future environment states through executable dynamics. WorldCoder [36]
further introduces a model-based interaction framework in which the agent explicitly writes and updates
executable world models represented as Python programs. Rather than storing environment knowledge
implicitly in model parameters alone, the agent maintains editable computational representations that can
be executed, revised, and reused during planning and interaction. Subsequent work extends this paradigm
toward continual and interactive world-model adaptation. RWML [129] combines execution traces with
reinforcement learning to refine environment dynamics through runtime interaction, while AWM [130] and
WorldMind [131] study how multiple executable world models can be aligned, fused, and coordinated across
tasks and knowledge sources.


_**2.3.3.**_ _**Code-Grounded Evaluation Environments**_


Code-grounded evaluation environments use executable systems as the interface for measuring agent behavior
and interaction quality. Unlike static benchmarks based solely on textual outputs, these environments
expose explicit runtime state transitions, execution feedback, and verifiable interaction outcomes that the
agent can directly observe and evaluate. InterCode [11] establishes this paradigm by reframing coding
tasks as interactive execution environments, where code acts as actions, execution feedback serves as
observations, and sandboxed runtimes provide grounded interaction. CRUXEval [132] further evaluates
program understanding through executable input-output prediction tasks, while LiveCodeBench [133]
introduces continuously updated evaluation pipelines that assess execution, self-repair, and runtime reasoning
capabilities under evolving problem distributions. SWE-bench [5] extends executable evaluation to real


<!-- source-page: 14 -->


world software repositories, where agents must modify large-scale codebases and are evaluated through
repository-level unit-test execution rather than textual correctness alone. More broadly, AgentBench [12]
demonstrates that executable interaction environments can evaluate reasoning and decision-making across
diverse embodied and digital tasks. Subsequent benchmarks such as CRUXEval-X [134], CoRe [135],
GeoGramBench [140], CodeGlance [136], and Endless Terminals [39] further expand this paradigm toward
multilingual, multimodal, and continuously interactive evaluation settings, where runtime interaction rather
than static answer matching becomes the primary evaluation interface.


_**2.3.4.**_ _**Verifiable Environment Construction**_


A newer direction treats executable environments not only as benchmarks to evaluate agents, but as harness
artifacts that can be synthesized, scaled, and validated programmatically. This is especially important
for long-horizon agents, where the harness must provide not only a task prompt, but also a runnable
state, transition dynamics, feedback channels, and verification oracles. SWE-smith [137] scales softwareengineering agent data by constructing repository-level tasks and execution environments from existing
codebases, turning software repositories into reproducible program worlds for agent training and evaluation.
EnvScaler [138] extends this idea beyond software engineering by programmatically synthesizing toolinteractive environments together with scenarios and rule-based trajectory validators. From the harness
perspective, these methods make the environment interface itself an object of construction: code specifies
not only what the agent edits or executes, but also the state transitions, tool affordances, and verifiers that
determine whether an interaction has succeeded.
