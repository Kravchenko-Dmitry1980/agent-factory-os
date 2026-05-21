---
source_pdf: "all.pdf"
chapter_number: 4
title: "Scaling the Harness: Multi-Agent Orchestration over Code"
source_page_start: 33
source_page_end: 47
---

# Chapter 4: Scaling the Harness: Multi-Agent Orchestration over Code

As AI systems tackle increasingly complex problems from function-level code synthesis to repository-level
system engineering, fundamental limitations for single-agent emerge: (1) context window constraints
prevent a single agent from holding an entire codebase, long interaction history, and execution trace in
working memory; (2) specialization requirements make it inefficient to use one generalist agent for planning,
synthesis, testing, review, and debugging simultaneously; and (3) the absence of independent coordination
and verification channels prevents the agent from reliably detecting and correcting its own errors during
long-horizon execution. Multi-agent systems introduce a powerful principle: once these responsibilities
are distributed across specialized roles, the agent harness itself becomes more modular, inspectable, and
adaptable. Early systems such as ChatDev [330], MetaGPT [55], and AgentCoder [50] demonstrate this
shift by dividing software-development responsibilities among distinct agents such as architect, programmer,
tester, reviewer, and executor. Coordinated through structured communication protocols and shared code
artifacts, these role-specialized agents turn code from a mere output target into the shared substrate through
which the overall harness plans, acts, verifies, and improves itself.


In this section, we systematically survey the rapidly growing direction on using MAS to scale coding harnesses,
and we propose a new position on building shared code-centric harness substrates for AI agents.


<!-- source-page: 33 -->


**Figure** 10: Overview of scaling the agent harness through multi-agent orchestration over code. The figure
illustrates how role-specialized agents, shared code-centric substrates, execution feedback, and adaptive
collaboration topologies address single-agent limitations in context, specialization, and self-correction.


**4.1.** **Improved Coding Support through Multi-agent Collaboration**


The most immediate contribution of multi-agent systems is that they improve coding support by decomposing the harness into specialized but coordinated components. Instead of integrating planning, synthesis,
execution, and verification into a single agent loop, these systems distribute responsibility across roles that
interact through shared code artifacts and feedback signals. This division of labor makes the overall harness
more capable of handling complex software tasks, while also making its internal workflow more inspectable
and controllable. In practice, this improvement is realized through three closely related design dimensions:
how roles are specialized, how agents interact over shared program artifacts, and how the workflow topology
organizes their collaboration.


_**4.1.1.**_ _**Functional Role Specialization and Human-Guided Planning**_


In human software development, different roles specialize in different aspects of the development process.
Many MAS naturally mirror this division of labor by assigning distinct functional roles to different agents.
This specialization allows each agent to focus on a specific slice of the shared code harness, leveraging its
unique capabilities and perspectives to contribute to the overall task. Here, we elaborate on the most common
functional roles identified across the surveyed literature, noting that many systems implement multiple roles
and that the boundaries between them can be fluid.


**Program synthesis agents** Program synthesis agents are responsible for generating or transforming code.
They consume specifications, plans, or feedback signals and produce or revise code artifacts. This is the most


<!-- source-page: 34 -->


**Figure** 11: Roadmap of scaling code harnesses for multi-agent orchestration, organized by workflow
collaboration, shared repository state, execution verification, and adaptive coordination.


common role across surveyed systems. Representative instances include the Coder in Self-Collaboration [56],
the Programmer in AgentCoder [50], the Engineer in MetaGPT [55], the Developer in ChatDev [330], and
the RTL Generation Agent in MAGE [339].


**Program understanding agents** Program understanding agents analyze existing code or specifications to
produce higher-level representations. They own the interpretation of what the code means rather than what


<!-- source-page: 35 -->


Table 9: Representative MAS collaboration designs by role specialization and interaction structure.


**System** **Harness Substrate** **Agent Roles** **Interaction Mode** **Topology**


Self- Blackboard, implicit Plan, Synth., Verif. Critique-repair Pre-defined cyclic
Collaboration [56] (simulated)


CodePori [331] Implicit Plan, Synth., Verif. Collab-Synth., Pre-defined chain, cyclic
critique-repair


MAGIS [332] Repository, evolution Plan, Understand, Critique-repair, Hierarchical, cyclic, dynamic pool
memory Synth., Verif. debate, delegation


HyperAgent [333] Repository, execution Plan, Understand, Critique-repair Pre-defined hierarchical, cyclic
Synth., Exec


PairCoder [334] Execution Plan-Understand, Collab-Synth., Pre-defined cyclic with conditional
Synth-Exec critique-repair branch


FlowGen [335] Execution, implicit Plan, Understand, Critique-repair, debate Pre-defined chain, cyclic (Scrum)
Synth., Verif.


Trae Agent [336] Repository, execution Generate, Prune, Collab-Synth., search Pre-defined search pipeline
Select (selection)


BOAD [337] Repository, execution Orchestrate, Localize, Delegation, adaptive Adaptive hierarchical
Edit, Validate selection


FlowReasoner [338] Execution, implicit Meta-design, Solve Runtime workflow Objective-driven adaptive
generation


ChatDev [330] Implicit, borderline Plan, Synth., Verif., Critique-repair, debate Pre-defined chain (waterfall)
exec Exec


MetaGPT [55] Implicit, partial Plan _×_ 3, Synth., Verif. Critique-repair, Pre-defined chain (waterfall)
blackboard pub-sub scheduling


GameGPT [210] Blackboard (dual Plan, Synth., Verif. Critique-repair, Pre-defined
collaboration) collaborative


it does. This category includes the Repository Custodian in MAGIS [332], the Navigator in HyperAgent [333],
the RepoUer in Lingma SWE-GPT [340], and the Column-type Annotator in CleanAgent [341].


**Verification agents** Verification agents evaluate code quality, typically by generating test cases, running
static analysis, or simulating execution. The Test Designer in AgentCoder [50] generates test cases independently of the code to avoid circular reasoning, a design principle against the mode-collapse problem where an
agent’s biased tests pass its own buggy code. The Test Quality Checker in QualityFlow [253] addresses this
at a meta-level, filtering synthesized tests before they are used as feedback. The Static Analyzer and Fuzzing
Agent in AutoSafeCoder [52] provide security-oriented verification through static CWE analysis and dynamic
crash detection, respectively. The Panelists in CANDOR [342] independently audit oracle correctness against
natural language specifications rather than against the code itself, deliberately avoiding contamination by
faulty implementations.


<!-- source-page: 36 -->


**Execution agents** Execution agents interface directly with the program runtime. Critically, the Test Executor
in AgentCoder [50] is a deterministic Python script (not an LLM) which cleanly separates reasoning from
execution and grounds the feedback signal in objective program behavior. The Executor in HyperAgent [333]
runs unit and integration tests via an interactive bash shell. The Judge Agent in MAGE [339] interfaces with
RTL simulation tools to produce per-clock-edge waveform snapshots.


**Planning** **agents** Planning agents decompose the overall software-development task into subtasks and
assign them to synthesis agents. The Architect and Project Manager in MetaGPT [55], the Manager in
MAGIS [332], the Scrum Master in FlowGen [335], and the Mother agents in SoA [212] all perform
task decomposition. The Mother agents in SoA [212] are particularly notable: they dynamically spawn
Child agents at runtime based on the inferred complexity of each subfunction, making planning and agent
initialization interdependent.


A distinctive feature of EvoMAC [328] is the introduction of two novel meta-roles not present in any other
surveyed system: the Gradient Agent, which reads execution logs to identify which agents caused failures,
and the Updating Agent, which revises agent prompts and restructures the workflow DAG accordingly. These
roles operate at the level of the MAS itself rather than the program, enabling the system to adapt its own
structure in response to execution feedback.


_**4.1.2.**_ _**Diverse Interaction Modes Grounded in Shared Program State**_


Unlike general MAS where agent interaction is primarily message-passing, code-centric interaction is characterized by artifact-mediated communication: agents observe and modify shared code artifacts, and their
interaction is grounded in the objective state exposed by those artifacts and their execution results. These
coordination channels are broader than source code alone: agents communicate through APIs, files, diffs,
tests, logs, schemas, blackboards, and explicit workflow states. In most systems, these channels are part of
the human-designed harness, while agents dynamically write to or modify the artifacts circulating within
them. We identify four interaction modes.


**Collaborative** **synthesis** Collaborative synthesis occurs when two agents jointly construct a program
component, analogous to pair programming [343]. The Navigator–Driver pairing in PairCoder [334] is the
most direct instantiation: the Navigator generates and selects solution plans while the Driver implements
them, with bidirectional information flow. CodePori [331] implements collaborative synthesis between
Dev_01 and Dev_02, who exchange code drafts across three rounds. This mode is relatively rare among the
surveyed system, as most systems prefer a sequential handoff rather than true co-construction.


**Critique and repair** Critique and repair is the dominant interaction mode across the surveyed literature.
A verification or evaluation agent inspects a code artifact and produces structured feedback; a synthesis
agent then revises the artifact in response. This pattern appears in some form in virtually every surveyed
system. Its key design decisions are: (a) whether the critique is LLM-simulated or execution-grounded
(Self-Collaboration [56] uses a simulated LLM tester, while AgentCoder [50] uses a real Python executor);
(b) the richness of the feedback signal (ranging from binary pass/fail in SEW [312] to structured execution
logs enumerating satisfied requirements, function errors, and unmet requirements in EvoMAC [328]); and
(c) the number of repair iterations permitted before fallback.


<!-- source-page: 37 -->


**Adversarial** **validation** Adversarial validation is a more active form of verification in which one agent
attempts to break the code through adversarial inputs, rather than passively reviewing it. AutoSafeCoder [52]
implements this via its Fuzzing Agent, which generates crash-inducing input seeds using type-aware mutation
and executes the code to produce crash traces. This mode has a fundamentally different character from
critique-and-repair: the fuzzer does not explain what is wrong, but demonstrates a concrete execution failure,
a counterexample that the coding agent must address. MAGE [339] similarly uses simulation mismatch as
an adversarial signal: the Debug Agent receives the exact waveform window around the first clock-edge
failure, enabling targeted repair.


**Reasoning** **debate** Reasoning debate involves agents arguing over the correctness of a decision or the
interpretation of a specification, before arriving at a consensus. ChatDev [330] introduces communicative
de-hallucination, a mechanism in which the assistant agent reverses roles to ask clarifying questions before
committing to a response. The Scrum sprint meetings in FlowGen [335] enable disordered multi-agent
discussion around a shared context buffer before the Scrum Master synthesizes a decision. CANDOR [342]
implements the most structured debate mechanism: three independent Panelists evaluate oracle correctness,
and a Curator aggregates their verdicts via majority vote. The kick-off meeting in MAGIS [332] involves a
circular speech among the Manager and all Developer agents to negotiate task dependencies and prevent
conflicts.


_**4.1.3.**_ _**Optimized Workflow Topology for Agentic Coordination**_


The topology of agent interaction, who communicates with whom, in what order, and how many times, is
one of the most consequential design decisions in a MAS for code generation. We organize topologies along
two primary axes.


**Pre-defined Heuristic Topologies** The majority of surveyed systems use topologies that mirror established
software development life cycle (SDLC) models. These topologies are fixed at design time and do not change
in response to task complexity or system performance.


_**Chain (Waterfall) topologies**_ sequence agents in a strict linear order, with artifacts flowing unidirectionally
from planning to synthesis to verification. ChatDev [330] and MetaGPT [55] are canonical examples,
explicitly modeling the waterfall SDLC: design _→_ coding _→_ testing. FlowGen [335] operationalizes three
SDLC models as distinct topologies: FlowWater (strict waterfall chain), FlowTDD (requirement _→_ design _→_
test _→_ implementation _→_ fix, a test-driven reordering), and FlowScrum (cyclic iterative sprints). This paper
is unique in directly comparing the implications of different SDLC-mirroring topologies for code quality.
L2MAC [344] also follows a chain topology but with a novel twist: each step in the instruction plan is
executed by a fresh-context agent, making the chain a sequence of independent LLM invocations sharing
only the external file store.


_**Cyclic**_ _**(Agile/Iterative)**_ _**topologies**_ introduce back-edges that allow code to be revised in response to
verification feedback. AgentCoder [50] implements a programmer _→_ test executor _→_ (if fail) _→_ programmer
cycle, bounded at 5 iterations. Self-Collaboration [56] embeds a coder _↔_ tester back-edge within its waterfall
chain, max 4 iterations. PairCoder [334] enhances the cyclic pattern with multi-plan exploration: a pool of
_n_ solution plans is pre-generated via k-means++ clustering for diversity, and the cycle can switch to the
next candidate plan when dead-end is detected through history-based loop analysis. MAGE [339] combines
a linear initialization chain with a cyclic debug-judge loop, and introduces high-temperature candidate
sampling to explore multiple program variants simultaneously.


<!-- source-page: 38 -->


_**Hierarchical**_ _**topologies**_ place one or more manager agents above a pool of worker agents, enabling
decomposition-and-delegation patterns. MAGIS [332] has a Manager that dynamically instantiates one
Developer agent per candidate file at runtime; each Developer edits its assigned file and reports back to the
manager-review layer. HyperAgent [333] uses a planner above multiple repository navigation and editing
workers, combining top-down decomposition with bottom-up repository evidence. SoA [212] pushes this
hierarchy further by allowing Mother agents to spawn Child agents recursively according to inferred subtask
complexity. These systems treat harness orchestration itself as a resource-allocation problem.


_**Star topologies**_ center on a hub agent that coordinates multiple parallel worker agents. The CANDOR [342]
Stage 3 panel is an example: a Requirement Engineer fans out to three independent Panelist+Interpreter
pipelines, and the Curator aggregates their outputs. MetaGPT [55]’s publish-subscribe message pool creates
a de facto star topology where the shared pool serves as the hub.


**Objective-driven** **and** **Adaptive** **Topologies** A smaller but rapidly growing class of systems treats the
topology itself as a design variable to be optimized toward a code quality signal. Recent systems such as
FlowReasoner [338] and BOAD [337] further reinforce this trend by treating multi-agent organization itself
as an adaptive object to be generated, searched, or optimized per task.


_**Dynamic**_ _**agent**_ _**pool**_ _**scaling**_ is the simplest form of adaptivity: the number of agents scales with task
complexity, but the topology type is fixed. SoA [212] implements this via a hierarchical tree of Mother
and Child agents, where Mother agents decide at runtime how many subfunctions to decompose into,
spawning corresponding Child agents. The key insight is that each agent’s context window remains bounded,
as complexity is handled by growing the agent pool rather than growing individual context windows.
MAGIS [332] similarly instantiates Developer agents dynamically based on the number of candidate files
identified during repository analysis. BOAD [337] extends this line of thought from dynamic scaling to
hierarchy discovery: instead of manually fixing the specialized sub-agent structure, it formulates the selection
of helpful localization, editing, and validation sub-agents as a bandit-optimization problem, showing that
automatically discovered hierarchical teams can outperform manually designed ones.


_**Feedback-driven**_ _**DAG**_ _**restructuring**_ is best represented by EvoMAC [328]. Its workflow is a DAG whose
nodes correspond to agents and whose edges define information flow. After each iteration, a Gradient Agent
reads execution logs to attribute failures to agents, and an Updating Agent modifies the prompts and graph
structure. This is the only system in the survey where the harness topology is structurally modified in response
to execution feedback.


_**Runtime self-reorganization**_ is SEW [312]’s approach: the system generates and mutates entire workflow
specifications using Direct Evolution (DE) and Hyper Evolution (HE) operators applied to LLM-generated
workflow descriptions in structured formats (BPMN, CoRE, Python, YAML). Rather than optimizing agent
parameters, SEW [312] optimizes the workflow structure including the sequence of agent calls, the routing
logic, and the feedback paths. The two canonical topologies it discovers (a linear chain and a feedback loop)
emerge from optimization rather than being hand-designed. FlowReasoner [338] pushes this adaptive view
further by training a query-level meta-agent that generates a tailored multi-agent system for each input
problem under external execution feedback, making topology selection itself part of the deliberative inference
process rather than a fixed system design.


<!-- source-page: 39 -->


Table 10: Representative MAS execution-feedback and convergence designs.


**System** **Harness Substrate** **Topology** **Execution Feedback** **Convergence**


_Pre-defined topology_


AgentCoder [50] Execution Cyclic Test pass/fail Correctness (test-gated)
MAGE [339] Execution (waveform) Chain-cyclic Checkpoint waveform Score-based correctness
MapCoder [44] Execution, implicit Cyclic Test pass/fail Correctness
AutoSafeCoder [52] Execution (static, fuzzer) Cyclic CWE warnings, crashes Security convergence
QualityFlow [253] Execution (real, imagined) Gated cyclic Pass/fail, imagined exec Correctness (quality-gated)
CodeCoR [166] Execution, implicit Cyclic Syntax, test pass/fail Score-based soft correctness
MARCO [345] Execution (performance) 2-node Cyclic Time, memory, FLOPS Performance, correctness


_Adaptive topology_


SoA [212] Execution, implicit gap Hierarchical tree Test pass/fail Correctness (implicit fallback)
SEW [312] Implicit Evolution Test pass/fail Implicit
EvoMAC [328] Execution Text DAG Compiler, execution logs Correctness (fixed-iteration)
FlowReasoner [338] Execution, implicit Query workflow Execution feedback Objective-driven adaptive
Trae Agent [336] Repository, execution Search pipeline Test, pruning signals Score-/selection-based


**4.2.** **Execution Feedback and Shared-Harness Synchronization**


We discuss how a group of agents can exploit the executability of code, and how they maintain a consistent
shared view of the program state. This dimension is the defining one for code-centric MAS: the shared
harness is uniquely executable and produces objective oracle signals. We address two sub-questions: what
types of execution feedback are used, and how is shared state synchronized across agents.


_**4.2.1.**_ _**Execution Feedback Integration**_


**Compiler** **and** **syntax** **feedback** Compiler and syntax feedback catch structural errors before runtime
and are used by many systems. ChatDev [330] feeds compiler errors from the testing phase back to the
programmer, though only as one-off corrections within a single phase. L2MAC [344] runs syntax checks
via its evaluator module _E_ ( _D_ ) after every file write, treating them as blocking conditions that prevent the
instruction pipeline from advancing.


**Test pass/fail signals** Test pass/fail signals are the most commonly used execution-feedback type. AgentCoder [50] centers its entire loop on whether independently generated test cases pass; the iteration terminates
on full pass or at the 5-iteration budget. QualityFlow [253] introduces a notable variant: Imagined Execution,
in which an LLM simulates the Python interpreter step-by-step and predicts test outcomes without actually
running the code, achieving 98%+ precision and recall on MBPP while avoiding label leakage from visible test
cases. The near-identical performance of Self-Collaboration [56]’s simulated LLM tester and its real-compiler
ablation raises a provocative empirical question: when is actual execution necessary, and when can linguistic
simulation of execution suffice?


**Fuzzer crash traces** Fuzzer crash traces represent a qualitatively different type of feedback: rather than
a pass/fail outcome, they provide a concrete failing input. AutoSafeCoder [52] uses type-aware mutation


<!-- source-page: 40 -->


to generate crash-inducing input seeds and passes the crashing input plus exit code to the Coding Agent.
This adversarial feedback is more informative than a generic failure signal because it localizes the bug to a
specific input category.


**Static** **analysis** **warnings** Static analysis warnings provide feedback about code structure and security
properties without execution. AutoSafeCoder [52] uses CWE-mapped static analysis against the MITRE
vulnerability database, enabling the Static Analyzer Agent to suggest remediation strategies keyed to specific
vulnerability classes.


**Performance** **profiling** **results** Performance profiling results are uniquely exploited by MACRO [345],
which treats code optimization as the primary task rather than correctness. The Performance Evaluator
Agent measures execution time, memory usage, and FLOPS, and MACRO [345] uniquely augments this with
real-time web search to retrieve relevant optimization techniques from the research literature.


**Fine-grained simulation feedback** MAGE [339]’s distinctive contribution is the finest-grained execution
feedback in the surveyed literature. Rather than reporting only whether a testbench passes or fails, the State
Checkpoint mechanism records signal values at every clock edge and delivers to the Debug Agent a waveform
window around the first failing clock cycle. This enables targeted repair at sub-test granularity.


_**4.2.2.**_ _**Shared-Harness Synchronization**_


Sequential handoff is the most common synchronization mechanism: each agent receives the output of its
predecessor and passes its own output to its successor. The program state exists only in the form of the most
recent artifact in the pipeline. This is sufficient for simple linear pipelines but creates invisible state divergence
in multi-agent settings where multiple agents modify the codebase in parallel or iteratively. It is also where
the limits of code-mediated coordination become clear. Even when agents share executable artifacts, the
harness still imposes information-theoretic constraints: channels have finite bandwidth, summaries introduce
compression loss, logs become noisy, cached views go stale, and parallel branches raise unresolved questions
of authority and consistency. Code provides a richer substrate for coordination, but it does not remove these
distributed-systems constraints.


**Shared blackboard** Shared blackboard provides a globally accessible program state that all agents can
read and update. L2MAC [344] implements this most cleanly: the file store _D_ is an external, persistent
structure that is never overwritten but extended and revised. The Control Unit manages all reads and writes,
ensuring that each agent invocation receives a precisely controlled context window. MAGIS [332]’s repository
evolution memory _M_ is a persistent key-value store mapping file versions to LLM-generated summaries,
updated incrementally via a specialized blackboard for repository-level reasoning. Self-Collaboration [56] is
among the first systems to explicitly name and invoke the blackboard architecture, establishing a shared
memory from which all three roles read and write.


**Parallel branches with merge** Parallel branches with merge arise when multiple agents modify independent
components simultaneously, with their changes integrated at a later stage. MAGIS [332] instantiates one
Developer per candidate file; each modifies its assigned file independently, and all changes are merged into


<!-- source-page: 41 -->


the final repository diff. HyperAgent [333] runs multiple Navigator and Editor instances in parallel via Redis
queues, with results merged at the Planner level.


**Structured context scheduling** Structured context scheduling is the explicit management of what each
agent sees and when. It is the primary innovation of L2MAC [344]. The Control Unit resets the context
window between instruction steps, providing each new invocation with a targeted summary of prior progress
( _Mrs_ ) rather than the full conversation history. When the context window approaches capacity, the Control
Unit stores partial results to _D_ and re-initializes with a compressed view, explicitly instructing the LLM
which files to read or skip given the remaining context margin. This mechanism solves the context-window
problem not by expanding the window but by carefully controlling its contents. MetaGPT [55] implements a
lighter form of context scheduling via a publish-subscribe message pool: each agent subscribes only to the
document types relevant to its role, receiving a filtered view of the shared state.


**Hierarchical memory** Hierarchical memory combines short-term working context with longer-term accumulated knowledge. ChatDev [330] explicitly separates short-term memory (full dialogue within a phase)
from long-term memory (extracted solutions carried across phases). Cogito [346] implements hierarchical
memory, drawing on neurobiological architecture: short-term memory for immediate task state, a long-term
knowledge base for accumulated expertise, and growth units for evolving abstractions that improve over
time. HyperAgent [333] uses a lightweight LLaMA-3.1-8B summarizer to condense execution logs before
storing them in hierarchical memory, preventing context bloat.


**Agent pool scaling** Agent pool scaling addresses the context-management problem orthogonally: rather
than managing what a single agent sees, it distributes the context load across more agents. SoA [212] is the
canonical example: by spawning more agents as task complexity grows, each agent’s context remains bounded.
This is a structural solution to the harness-state problem: instead of building a shared representation that
all agents can query, SoA [212] partitions the task state across agents, each holding a bounded slice. The
limitation is that global consistency is sacrificed: agents cannot reason about the full program, only their
assigned sub-function.


**Other** QualityFlow [253]’s revert mechanism represents a synchronization pattern: the initial code artifact
is never overwritten, enabling the system to roll back to a prior shared harness state if the debugging
trajectory degrades quality. This is the only work among the surveyed system that explicitly manages state
history rather than always moving forward.


**4.3.** **Position:** **The Shared Code-Centric Harness Substrate**


We propose a new position for the next generation of multi-agent intelligence: the shared code-centric
harness substrate. This position is motivated by the central gap identified in the literature: the lack of formal,
persistent representations of the shared code state that agents can query and update across iterations. We
argue that building such a harness substrate is both feasible and necessary for achieving robust, scalable
multi-agent intelligence.


<!-- source-page: 42 -->


Table 11: Representative MAS designs centered on shared program-state representation and synchronization.


**System** **Harness Substrate** **Agent Roles** **Execution Feedback** **Convergence / Synchronization**


L2MAC [344] Blackboard, repository, Plan, Synth, Verif Syntax, test pass/fail Correctness per instruction step
execution (evaluator)


Cogito [346] Blackboard (3-tier Neurobiological model NA Hierarchical memory
memory) synchronization


CleanAgent [341] Execution (weak), Plan, Understand, Runtime errors Correctness through execution
implicit Synth, Exec success


Lingma Repository, execution Understand, Syntax, git apply, tests Fixed-limit implicit convergence
SWE-GPT [340] Synth-Verif


SyncMind [347] Repository, execution Synth-Understand, Test pass/fail, runtime Correctness, resource-constrained
(formal _Sk_ / _Bk_ ) oracle Understand errors synchronization


BOAD [337] Repository, execution Orchestrator with Test pass/fail, Hierarchy discovery, coordination
specialized sub-agents validation reward


CANDOR [342] Execution (Java, Plan, Synth, Verif, Compiler, coverage, Correctness, coverage, consensus
JaCoCo) Understand, Debate tests


_**4.3.1.**_ _**Shared Harness Representation**_


A foundational question for any MAS is: what is the substrate these agents inhabit? In code as agent harness,
the natural answer is the shared program environment, namely the collection of artifacts, execution contexts,
and quality signals that agents collectively act upon and that evolve as agents produce, revise, and evaluate
code. We call this the shared harness substrate, and we distinguish four levels of formalization with which
existing systems represent it.


**Implicit / File-only Representation** The most common and least formalized category treats the shared
harness as simply the current code file or set of code files. Agents receive the latest code artifact as part of
their input context and produce a modified or evaluated version. There is no persistent, queryable representation: the shared state is reconstructed implicitly at each agent invocation from the conversational history.
This category encompasses many foundational systems: ChatDev [330], MetaGPT [55], FlowGen [335],
MapCoder [44], CodeCoR [166], SEW [312], and CodePori [331]. While this representation is simple to
implement, it entails a fundamental limitation: agents cannot reason about the shared substrate except
through the narrow lens of their most recent context window. State divergence [347], in which an agent’s
internal belief about the code state diverges from the true state, is invisible to the system and cannot be
detected or corrected.


**Repository-based Representation** A richer class of systems represents the shared harness as a navigable
repository: a file system with directory structure, inter-file dependency graphs, call hierarchies, and version
history. This representation supports agents that reason about where in the codebase a change needs to be
made, what other components depend on the changed function, and how the codebase has evolved over time.
MAGIS [332] introduces a repository evolution memory that caches file-level summaries and incrementally
updates them via git diff as files change across issue-resolution episodes. HyperAgent [333] provides agents
with repository navigation tools (get_tree_structure, go_to_definition, code_search, get_all_references),


<!-- source-page: 43 -->


treating the repository as a structured knowledge base. Lingma SWE-GPT [340] compresses the repository
view via abstract syntax tree (AST) skeletons, preserving function signatures and class definitions to enable
efficient navigation. SyncMind [347] is the only work to formally define the repository substrate as a
ground-truth state _Sk_ and measure the divergence between _Sk_ and an agent’s belief state _Bk_ .


**Execution-based** **Representation** Execution-based representation is the most distinctive category for
code generation. It has no direct parallel in general MAS and represents the shared substrate through
execution behavior. The state is not what the code looks like but what the code does: whether it compiles,
which tests it passes, what vulnerabilities a fuzzer uncovers, how fast it runs, and whether its runtime
behavior matches its specification. This execution-based representation provides an objective oracle signal, a
ground truth that is not subject to the hallucination or bias that affects purely linguistic agent evaluations.
Systems that exploit this representation include AgentCoder [50], AutoSafeCoder [52], QualityFlow [253],
MACRO [345], EvoMAC [328], CANDOR [342], and MAGE [339]. Notably, MAGE [339] achieves the
finest-grained execution feedback in the literature, operating at clock-edge granularity via _State Checkpoint_
waveform snapshots.


**Blackboard / Shared-State Representation** A fourth category introduces an explicit, globally accessible
data structure that all agents can read from and write to (akin to the classical blackboard architecture in
AI [348]). This shared state is the closest approximation in the literature to a formal harness substrate: it
persists across agent invocations, can be queried and updated, and provides a consistent view of the program
state to all agents. Self-Collaboration [56] is among the first systems to explicitly invoke the blackboard
metaphor, establishing a shared memory from which all three roles (Analyst, Coder, Tester) read and write.
L2MAC [344] implements the most principled blackboard in the literature: a persistent file store _D_ with
semantically meaningful paths, accessed through a Control Unit that explicitly manages which slice of state
each agent invocation sees. GameGPT [210] uses a shared context buffer to reduce redundant information
retransmission in multi-round game development. Cogito [346] draws on neurobiological architecture to
implement a three-tier memory: short-term working state, long-term knowledge base, and growth units for
evolving abstractions, as a structured harness representation.


**The Central Gap** The distribution of systems across these four categories reveals a striking pattern: the
majority of the literature resides in the implicit/file-only category, lacking any formal model of the shared
harness substrate. This is the central gap that motivates the code as agent harness framing. The program,
uniquely among multi-agent domains, is an artifact that executes. It produces objective, non-linguistic signals
that could in principle anchor a formal shared substrate. Yet most systems fail to exploit this property at the
architectural level, instead relying on agents to reason about code quality through natural language alone.


_**4.3.2.**_ _**Harness-State Convergence**_


Convergence determines when a multi-agent coding harness should stop iterating and accept its current
program state as a satisfactory outcome. In many existing MAS, convergence is still defined implicitly,
either by consensus among agents or by an external iteration budget. However, code as agent harness has a
distinctive advantage: because the shared substrate is executable, convergence can be grounded in objective
behavioral signals rather than in conversational agreement alone. We identify six convergence patterns,
ranging from widely used test-gated and implicit convergence to less common security-, performance-, and
consensus-based criteria.


<!-- source-page: 44 -->


**Correctness convergence** Correctness convergence (test-gated) is the most principled and widely used objective criterion: the system terminates successfully when all test cases pass. AgentCoder [50], L2MAC [344],
SyncMind [347], and CANDOR [342] implement test-gated convergence. PairCoder [334] augments this
with dead-end detection: if the same buggy code or feedback appears in the iteration history, the system
switches to the next candidate plan rather than looping. FlowGen [335] uses test-gated convergence but on
LLM-generated tests rather than ground-truth tests, introducing a potential quality concern: a system can
converge on code that passes its own biased tests but fails on external evaluation.


**Security convergence** Security convergence is uniquely implemented by AutoSafeCoder [52]: the system
terminates successfully when no CWE vulnerabilities are flagged by static analysis and no crashes are induced
by the fuzzer. This multi-criteria convergence is a strong argument for the execution-based harness framing.
Both convergence criteria are grounded in objective program behavior, not agent opinions.


**Performance convergence** Performance convergence is the focus of MACRO [345]: the optimization loop
terminates when user-defined runtime and memory thresholds are satisfied, as measured by the Performance
Evaluator against actual execution benchmarks. This is the only system that treats performance as the
primary convergence criterion rather than correctness.


**Score-based convergence** Score-based convergence uses quantitative quality scores computed by agents
evaluating intermediate outputs to determine when to stop. MAGE [339] ranks candidate programs by
their simulation mismatch score _s_ ( _r_ ) = 1 _−_ _m_ ( _r_ )/ _tc_ ( _r_ ) and continues iterating until the maximum score
reaches 1.0. CodeCoR [166] uses a four-criteria binary score (clarity, relevance, conciseness, context) to
prune intermediate outputs at each agent stage and selects the highest-ranked code in its Ranked Code
Set as the final output. It sets a soft correctness convergence that submits the best available result rather
than waiting for a perfect solution. Trae Agent [336] introduces a closely related search-and-selection view
at repository scale: it formulates issue resolution as an optimal solution search problem and uses modular
generation, pruning, and selection agents to navigate a large ensemble space of candidate patches. In this
setting, convergence is not only a matter of repeated repair, but also of ranking, filtering, and selecting
among competing solutions under repository-aware evidence.


**Consensus convergence** Consensus convergence aggregates judgments from multiple reviewer agents.
CANDOR [342] implements majority voting among three Panelists on oracle correctness. MAGIS [332] uses
LLM-judgment from the QA Engineer as the acceptance signal, though this is a single-agent consensus rather
than a multi-agent vote. QualityFlow [253] uses its Code Quality Checker as the single gating signal. It is an
efficient design where the quality checker serves as both a convergence oracle and the system controller,
enabling early exit (75–84% of problems converge after the first generator call).


**Implicit convergence** Pipeline termination after a fixed number of stages or iterations with no objective
quality criterion is the most prevalent convergence pattern in the literature and represents the most significant
gap in the field. ChatDev [330] terminates after a fixed number of phases, or when two consecutive rounds
produce identical code, or after 10 rounds, none of which is an objective quality signal. MetaGPT [55]
terminates after completing the fixed SOP stages. Self-Collaboration [56] falls back to implicit convergence
after _n_ = 4 iterations if the tester never approves. EvoMAC [328] runs a fixed _K_ iterations of the textual


<!-- source-page: 45 -->


backpropagation loop. The prevalence of implicit convergence is a direct consequence of the lack of formal
shared substrates: without an objective representation of the program state, systems have no principled
criterion for convergence.


**4.4.** **Patterns and Trends**


Across systems, differences in role specialization, shared-state representation, execution grounding, and
workflow topology are not independent engineering choices; they interact to determine how reliably a group
of agents can maintain coherence over long-horizon coding tasks. In this subsection, we distill the main
trends that emerge from the surveyed systems, highlighting both the common structural bottlenecks of
current systems and the design principles that point toward more robust shared harnesses.


**The implicit-harness-state constraint** The majority of surveyed systems (ChatDev [330], MetaGPT [55],
FlowGen [335], CodePori [331], SEW [312], MapCoder [44], CodeCoR [166]) operate without explicit
representations of the shared code harness. These systems rely on agents to reconstruct state implicitly
from conversational history at each invocation. This design choice works for function-level tasks where
the program state is simple and does not fragment across agents. However, this implicit approach creates
a fundamental vulnerability: without a formal shared substrate, agents cannot reliably detect when their
internal understanding diverges from the true program state [347]. From the code as agent harness
perspective, the reliance on implicit state representations is the technical root of system brittleness rather
than a scalability convenience.


**Code-mediated channels do not eliminate coordination bottlenecks** The shift from free-form dialogue
to code-mediated coordination is a genuine architectural advance, but it should not be overstated. Files,
APIs, diffs, tests, logs, schemas, blackboards, and workflow states are all partial channels through which task
state is encoded, transmitted, and reconstructed. Each channel trades off fidelity, latency, and scope: tests
compress semantics into pass/fail, summaries save context at the cost of detail, logs are grounded but noisy,
and shared blackboards improve persistence while creating authority and consistency problems. The central
design question is therefore not merely whether code is present, but which artifacts are authoritative, how
they are compressed, and how conflicts across channels are resolved.


**Execution** **feedback** **as** **the** **bridge** **between** **linguistic** **and** **formal** **reasoning** The deepest divide in
the literature is between systems that use execution as ground truth and those that rely on linguistic
model judgments. Systems that ground shared state in execution (AgentCoder [50], AutoSafeCoder [52],
QualityFlow [253], EvoMAC [328], MAGE [339]) have access to objective oracle signals, signals that cannot
hallucinate. Yet a surprising finding complicates this picture: Self-Collaboration [56] and QualityFlow [253]
demonstrate that LLM-simulated execution can achieve 98%+ precision and recall in predicting actual
outcomes without running code. This suggests that execution feedback’s value is not uniform across all
failure modes. It excels at detecting the corner cases that linguistic simulation structurally cannot imagine
(runtime crashes, resource exhaustion, boundary condition errors, performance regressions), but for many
correctable bugs, simulated reasoning may suffice. A mature harness would integrate both: using linguistic
reasoning as the fast path and delegating to execution as the verification oracle only for the failure modes
that require it.


<!-- source-page: 46 -->


**Two** **complementary** **representations** **of** **the** **shared** **harness** The surveyed systems reveals two conceptually orthogonal views: repository-based representation (structure: what functions call what, where
does data flow, what are the dependencies) and execution-based representation (behavior: what does the
code do when run, how does state evolve at runtime, what emergent failures occur under different inputs).
MAGIS [332] and HyperAgent [333] operate primarily in the repository view, enabling agents to reason
about codebase architecture. AgentCoder [50] and MAGE [339] operate primarily in the execution view,
grounding shared state in runtime signals. Yet none of the surveyed systems fully unifies both views into a
single harness substrate where agents can reason across both the static structure of code and its dynamic
behavior. The deepest harness would integrate these two perspectives, answering questions like “which
components are slow” (requires both call graphs and profiling data) or “does this refactoring break APIs that
external code depends on” (requires both static analysis and dynamic testing).


**Topology complexity inversely correlates with harness-state formality** Systems with explicit, formal
shared substrates use simpler topologies, while systems lacking formal shared state employ increasingly
complex topology patterns as a structural workaround. L2MAC [344], which has the clearest formal harness
substrate (a persistent file store with explicit context scheduling), uses a simple sequential chain with
sophisticated state management. By contrast, implicit-state systems like EvoMAC [328] and SEW [312]
develop elaborate adaptive topologies (dynamic DAGs, workflow mutation, agent pool scaling) that attempt
to optimize the collaboration structure in the absence of a principled shared representation. This suggests
that topology complexity is partially a symptom: when the substrate is formally represented and queryable,
agents can coordinate through simple, transparent protocols. When the substrate is implicit, agents require
richer interaction patterns to compensate for missing state information.


**Context management is the tax of implicit shared state** A striking pattern is that many systems have
developed sophisticated context-management mechanisms precisely because they lack a formal shared
substrate. L2MAC [344]’s Control Unit, MetaGPT [55]’s publish-subscribe pool, SoA [212]’s agent-pool
scaling, and Cogito [346]’s three-tier memory are all responses to the same underlying problem: how to
give agents a coherent view of a code harness that is too large to fit in any one context window. A mature
harness substrate could unify these disparate solutions by providing a principled, queryable representation
of task state that agents access on demand, rather than forcing the system to carefully manage what each
agent sees at every step.


**Agent specialization increases the criticality of shared state metrics** As agent role diversity increases,
from basic coder-tester pairs to systems with Architect, Manager, Navigator, Executor, and Verifier roles,
the need for a unified shared substrate becomes urgent. Without shared understanding of code state, the
Planning Agent may decompose tasks based on an outdated codebase snapshot, the Execution Agent may
run tests against a different version than the Synthesis Agent intended, and the Verification Agent’s feedback
may misfire. EvoMAC [328] addresses this through its Gradient and Updating agents that explicitly monitor
failure attribution at the MAS level. SyncMind [347] formalizes the problem as agent belief divergence
_|Bk −_ _Sk|_, proposing explicit synchronization protocols. The proliferation of agent roles is thus not merely
an engineering choice. It is a forcing function for developing more mature shared harnesses. Multi-agent
systems with rich role repertoires cannot function robustly without them.


<!-- source-page: 47 -->


**Figure** 12: Overview of code as an agent harness across five emerging domains, including coding assistants,
GUI/OS agents, scientific discovery, personalization, and embodied agents.
