---
source_pdf: "all.pdf"
chapter_number: 3
title: "Harness Mechanisms: Planning, Memory, Tool Use, Control, and Optimization"
source_page_start: 15
source_page_end: 32
---

# Chapter 3: Harness Mechanisms: Planning, Memory, Tool Use, Control, and Optimization

Harness mechanisms form the central systems layer that makes code-harnessed agents reliable beyond a
single generation step. Once code enters the agent loop, software generation is no longer only a problem of
producing correct programs from a prompt. It becomes an interaction among the model, mutable task state,
and human-designed harness infrastructure. The model provides judgment: it decomposes goals, selects
actions, interprets feedback, and decides when to revise. Mutable state records repository evidence, working
context, execution traces, validation results, memories, and intermediate beliefs about the task. The harness
infrastructure exposes tools and execution substrates, persists and compacts state, constrains actions through
policies and permission tiers, routes feedback, and verifies whether each state transition is acceptable. From
this perspective, harness mechanisms are not isolated add-on modules, but coordinated control surfaces that
turn model decisions into bounded, observable, and revisable changes in an executable environment. In its
basic form, code allows the agent to call existing executable interfaces. Further, the agent can dynamically
author task-specific executable interfaces. These agent-authored artifacts make the harness more adaptive
because they allow the execution environment to be reshaped around the current task. However, dynamically
authored code does not replace the broader human-designed harness infrastructure. Reliability still depends
on model-side judgment together with human-designed policies, sandbox boundaries, permission tiers,
verification oracles, audit logs, and human-review gates. Code therefore serves as an executable medium
inside the harness, while the harness remains the larger policy-governed system that decides what code may
be executed, trusted, persisted, reused, or promoted into future workflows.


In this section, we review five interacting categories of harness mechanisms for code agents. Planning (§ 3.1)
organizes long-horizon task execution by externalizing goals into decompositions, structural constraints,
search trajectories, or workflow-level orchestration. Memory and context engineering (§ 3.2) manage
mutable state across long interactions by preserving working context, retrieving repository evidence, storing


<!-- source-page: 15 -->


**2023** **2024** **2025** **2026**


**Planning**


**Memory**


**Tool Use**


**Control**


**Optimization**


**Figure** 4: A roadmap overview of agent harness mechanisms.


reusable experience, supporting shared histories, and offloading state beyond the active context window. Tool
usage (§ 3.3) connects the agent to governed executable interfaces, including APIs, repositories, terminals,
sandboxes, verification tools, and workflow orchestrators. Harness control through the Plan-Execute-Verify
loop (§ 3.4) reframes feedback-guided debugging as a broader control process: plans form contracts over
intended changes, execution applies them inside sandboxed and permissioned environments, and verification
uses deterministic sensors and human-review gates to decide whether the state should be accepted, revised,
escalated, or rolled back. Finally, agentic harness engineering (§ 3.5) studies how the harness itself can be
measured and improved through deep telemetry, evolution agents, replay-based evaluation, and governed
harness mutation.


**3.1.** **Planning for Agent Harness**


Planning plays a central role in agentic harness because real-world software engineering tasks rarely admit
a direct one-shot mapping from natural language intent to correct implementation. From the harness
perspective, planning is not merely an internal reasoning capability of the LLM, but a form of _harness control_ :
it structures how the agent externalizes intent into executable steps, schedules interactions with code artifacts
and tools, and regulates the trajectory of reasoning, execution, and revision over time. Beyond generating
code tokens, an effective agent harness must organize long-horizon problem solving into a coherent course of
action, deciding what intermediate goals to pursue, in what order to execute them, what artifacts to inspect
or modify, and how to revise the trajectory when execution feedback reveals errors, missing dependencies, or


<!-- source-page: 16 -->


**Figure** 5: Overview of planning mechanisms for agent harnesses.


violated constraints. This need becomes especially pronounced in repository-level editing, web interaction,
competitive programming, and hardware design, where the agent must operate over large action spaces,
sparse feedback, and deeply interdependent subproblems. In such settings, a fundamental challenge arises
**between the complexity of the target task and the limited reliability of unconstrained agent execution** :
without an explicit planning mechanism as harness control, the agent may commit too early to brittle solution
paths, overlook latent dependencies, or fail to coordinate reasoning, retrieval, execution, and revision into a
stable workflow.


Early planning-oriented systems mainly treated planning as a linear decomposition step, where the model first
produced a natural-language solution outline and then translated it into code. As code agents were applied to
more complex environments, however, planning gradually evolved from a simple pre-generation scaffold into
a richer harness-level control mechanism. It can be grounded in repository structure or external knowledge
to constrain the agent’s action space, expanded through explicit search over multiple candidate trajectories to
improve robustness, or distributed across specialized agent roles and feedback loops to coordinate execution
at the system level. Based on the **primary locus where harness control is realized**, we categorize existing
planning methods in code agents into four types: _linear decomposition planning_, _structure-grounded planning_,
_search-based planning_, and _orchestration-based planning_ .


_**3.1.1.**_ _**Linear Decomposition Planning**_


In this planning paradigm, the agent first produces a single explicit, executable sequence of steps, and then
carries out generation by following this decomposition [141, 40, 41, 142, 143]. A lightweight precursor
of this pattern is ReAct [144], where the agent interleaves thoughts, actions, and observations in a serial
trajectory. In this framework, each reasoning step externalizes the current subgoal and constrains the
next action, turning the trajectory itself into a stepwise harness for control. This pattern is most directly
instantiated in Self-Planning [40]: the model first decomposes the intent into concise, high-level numbered
steps, and then generates code step by step under the guidance of this plan. Plan-And-Act [145] further
makes this harness explicit by separating a planner, which produces structured high-level plans: the planner
repeatedly refreshes the linear scaffold as new observations arrive, allowing the planning strategy to preserve
task-level control while adapting to environmental feedback. WebAgent [41] extends this idea to web


<!-- source-page: 17 -->


automation: it decomposes a user instruction into successive sub-instructions, summarizes task-relevant
HTML conditioned on the current subgoal, and then synthesizes executable Python actions from that linear
sub-instruction sequence. KareCoder [141] follows a similar template in a knowledge-augmented setting,
where the model first constructs a knowledge-aware, step-by-step prompt from an external knowledge library
and then uses this prompt to generate code, making planning a structured intermediate layer between
problem understanding and implementation. Recent industrial practice shows that this linear scaffold can be
lifted from an ephemeral prompt artifact to a persistent harness object. In long-horizon coding workflows,
files such as `PLAN.md`, `Implement.md`, and status logs record milestones, acceptance criteria, validation
commands, and recovery rules, allowing the agent to reload, update, verify, and document progress across
context resets or multi-session execution [146, 147]. In this view, planning is no longer merely an internal
reasoning trace, but a filesystem-backed control object: it can be reviewed by humans, versioned with Git,
consumed by subagents, and used as the source of truth for implementation. The main limitation remains
that these methods typically commit to a single decomposition trajectory: when the initial plan is incomplete
or misaligned, the harness can improve persistence and auditability, but it still provides limited exploration
beyond the chosen path.


_**3.1.2.**_ _**Structure-grounded Planning**_


In this line of work, the agent does not derive its action sequence solely from a free-form natural language
prompt, but instead grounds planning in an explicit structured representation of the task environment, such
as dependency graphs, repository graphs, circuit graphs, or knowledge graphs. These structures act as natural
harness scaffolds: they expose relevant entities, encode dependency relations, and guide the order in which
subtasks should be generated, revised, or verified. For example, CodePlan [42] constructs a plan graph
over edit obligations and derives new steps through dependency analysis and change-impact propagation.
Meanwhile, repository understanding methods [148, 149, 150, 148] convert codebases into heterogeneous
graphs or text-rich code graphs, then use graph-integrated reasoning to localize relevant entities and condition
downstream generation on structural dependencies rather than flat text context. GraphCodeAgent [151]
extends this idea with a dual-graph harness, where a Requirement Graph captures relations among naturallanguage requirements and a Structural-Semantic Code Graph captures repository dependencies. The same
principle also appears in recent agent-native repository practices. Files such as architecture notes, API
specifications, and testing guides turn project knowledge into persistent, inspectable, and version-controlled
artifacts that the agent can consult before acting [152, 153, 154]. This broadens structure-grounded planning
beyond graph construction: the relevant structure determines explicit rules, build commands, directory
boundaries, coding conventions, and design constraints, thereby promoting a coherent and stable harness
control over the programs. Specialized domains follow the same pattern [155, 156]. VerilogCoder [156]
grounds subtask planning in a Task and Circuit Relation Graph so that each subtask is enriched with signals,
transitions, and examples, while DomAgent [155] uses knowledge graphs to combine top-down structured
knowledge with bottom-up examples for domain-specific code generation. Overall, these works show that
structure-grounded planning improves coherence, dependency awareness, and long-horizon consistency by
turning project or domain knowledge into explicit and inspectable harness objects that guide the agent’s
behavior over time.


_**3.1.3.**_ _**Search-based Planning**_


Search-Based Planning allocates inference-time compute to systematically explore, evaluate, and select
among multiple candidate solution paths. Rather than committing the agent to a single plan, the key idea is
to expand the decision space and use feedback to control which alternatives should be pursued, revised, or


<!-- source-page: 18 -->


Table 4: Representative planning modules for code agents.


**Method** **Category** **Core Mechanism** **Interface** **Feedback**


Self-Planning [40] Linear decomposition Stepwise decomposition Shared prompt None
WebAgent [41] Linear decomposition Sub-instruction sequencing APIs Runtime exception
CodePlan [42] Structure-grounded Plan graph Repo graph Critique
VerilogCoder [156] Structure-grounded Task-circuit relation graph Repo graph Test pass/fail
Tree-of-Code [159] Search-based Trajectory tree search Execution env Test pass/fail
ReThinkMCTS [158] Search-based MCTS over reasoning paths Execution env Critique, tests
MapCoder [44] Orchestration-based Role orchestration APIs Critique, tests
Blueprint2Code [165] Orchestration-based Blueprint-to-code Repo interface Critique


discarded. A first group of methods [157, 158] instantiates this harness in the thought space. Instead of
directly writing code, they first branch over high-level observations, strategies, or reasoning traces, with
the goal of increasing conceptual diversity before implementation. In this view, better planning comes from
covering a broader idea space and using feedback to refine reasoning itself, rather than merely repairing final
code. A second group [43, 159, 160, 161] performs search in the trajectory space of coding actions: these
methods model coding as a branching process over strategy choice, implementation, debugging, and revision,
and rely on execution signals or learned critics to decide which nodes to expand. Therefore, long-horizon
coding quality improves when the agent can backtrack from suboptimal decisions and compare partial
trajectories. Another line of these works, such as ReLoc [162] and SFS [163], treats planning as search in
code space. Here the methods iteratively explore neighboring programs through mutation, revision, or local
optimization, guided by validation feedback or fine-grained scoring signals. Beyond the above methods,
recent systems increasingly treat candidate plans, patches, logs, tests, and execution traces as persistent
artifacts rather than transient generations. SWE-Search [164] combines Monte Carlo Tree Search with
software-engineering agents to explore alternative repair trajectories, while CodeTree [43] organizes strategy
exploration, solution generation, and refinement within a unified tree. More broadly, Meta-Harness [13]
pushes this idea to the harness level itself: it searches over harness code by giving an agent access to prior
source code, scores, and execution traces through a filesystem. These developments suggest that search-based
planning is not only a model-side sampling strategy, but also a harness-level state management problem:
the runtime must preserve candidates, expose evidence, run validators, and decide which branch deserves
further computation.


_**3.1.4.**_ _**Orchestration-based Planning**_


Orchestration-Based Planning refers to a planning paradigm in which the core planning function is realized
through a harness design for system-level coordination. In this paradigm, the harness governs how agents or
modules specialize roles, execute stages, route feedback, and trigger verification loops, thereby determining
what actions should be taken next in long-horizon code generation workflows. A first common pattern [50,
51, 52] is feedback-centered orchestration, where the system distributes coding, testing, analysis, and repair
across different modules, so that progress is driven by repeated execution-grounded feedback and adaptive
escalation. In this group, planning is not an up-front artifact, but an emergent property of how failures
are detected, interpreted, and routed back into subsequent actions. A second pattern [44, 166, 165] is
staged workflow orchestration, which casts code generation as a structured software-process pipeline, such
as comprehension, retrieval or preview, planning or blueprinting, coding, debugging, and repair. The main
advantage of this group lies in decomposing complex generation into interpretable stages with explicit
handoff rules, and the actual planning power comes from cross-stage control, candidate pruning, and


<!-- source-page: 19 -->


iterative refinement. A third pattern [167, 168, 169, 170] is controller-centric orchestration, where planning
is embedded in the transformation of intermediate artifacts and in the routing substrate itself. Here, systems
organize decision-making through mechanisms such as formal-specification pipelines, suggestion stages
between localization and repair, typed intermediate representations, shared blackboards, or specialized
planner–coder coordination, so that the next plan is determined by the scaffold’s control logic rather than by
a single textual prompt.


Recent harness systems make this orchestration view especially explicit. Anthropic’s long-running harnesses
separate planning, generation, and evaluation into distinct roles, using structured artifacts and independent
evaluation to maintain progress across long sessions [15, 171]. Cursor’s large-scale autonomous coding
experiments similarly highlight planner–worker coordination as a way to scale from focused single-agent
tasks to many parallel agents working on a shared project [172]. The most general formulation appears in
Natural-Language Agent Harnesses, where high-level harness logic (such as roles, stages, contracts, adapters,
state conventions, and failure taxonomies) is written as editable natural language and executed by an
Intelligent Harness Runtime [173]. The IHR interprets these high-level natural-language instructions at
runtime and converts them into constrained execution steps under explicit contracts, budgets, tool interfaces,
and environment state. This reframes orchestration-based planning as a runtime interpretation problem:
the plan is not merely a document, but an executable harness specification that mediates between model
outputs, filesystem state, tools, validators, and multi-agent delegation.


_**Discussion:**_ Planning for code generation can be understood as a core form of _agentic harness_ : a control
layer that organizes how an LLM agent decomposes tasks, grounds decisions in program structure, explores
alternatives at inference time, and coordinates multi-stage software engineering workflows. From this
perspective, planning is a set of harness mechanisms centered on one essential question: how to decide what
the agent should do next, and how to keep that decision process constrained, inspectable, and coherent
across long-horizon coding tasks. Notably, planning in code generation cannot be cleanly separated from
the evaluation problem. Many current conclusions about the benefits of planning depend heavily on the
surrounding execution conditions, including execution environments, feedback quality, tool access, trajectory
budgets, and whether the benchmark truly stresses long-range dependency management rather than localized
patch generation. If execution signals are weak, revision budgets are unrealistic, or benchmarks fail to expose
multi-step coordination errors, then reported planning gains may not reflect genuine improvements in agentlevel problem solving. Therefore, planning is not only a method design problem, but also a harness problem
between the agent and the environment. Looking forward, the central challenge is not merely to build larger
planners or longer reasoning traces, but to design more reliable agentic harnesses for planning: adaptive
commitment mechanisms that decide when to follow, revise, or abandon a plan; structurally meaningful
planning states that expose dependencies and progress; efficient exploration-and-revision strategies that use
feedback without excessive computation; and rigorous long-horizon evaluation paradigms that can faithfully
measure planning quality beyond final-pass accuracy.


**3.2.** **Memory and Context Engineering for Agent Harness**


Memory has become a core infrastructure for code agents, largely because real-world software engineering
tasks are inherently long-horizon and state-intensive [174, 175]. Unlike single-turn code completion, practical
coding scenarios require an agent to sustain a sequence of interdependent steps across many rounds of
interaction, such as requirement understanding, code localization, evidence retrieval, multi-file editing,
test execution, bug fixing, and regression verification [176, 177]. This introduces a fundamental tension

**between the limited context window of the model and the continuously expanding intermediate state**
**of the task** . From a harness perspective, memory is not simply a larger context window or a vector database.


<!-- source-page: 20 -->


**Figure** 6: Overview of memory and context engineering mechanisms for agent harnesses.


It is a state-management layer that decides which information should remain in the active model context,
which information should be compacted into summaries, and which information should be offloaded to
durable external storage [178]. Without an effective memory mechanism and context management, an agent
can easily lose critical clues during long-range reasoning, repeat searches and analyses that were already
completed, or break local consistency established in earlier steps during later modifications [179, 175].


Early systems largely relied on prompts to preserve historical information, treating memory as little more
than conversation history or an unstructured scratchpad. However, with the emergence of repository-level
repair and other long-horizon coding tasks, it has become increasingly clear that simply accumulating natural
language history cannot reliably support complex software engineering loops [180]. As a result, memory is
now increasingly externalized as a system component that is retrievable, governable, and traceable. In this
subsection, we categorize memory in code agents according to their **primary functional role** in the software
engineering loop. Under this view, existing approaches can be broadly organized into five types: _working_
_memory,_ _semantic memory,_ _experiential memory,_ _long-term memory,_ _and multi-agent memory_ . In addition,
we discuss context compaction and state offloading as cross-cutting context-engineering mechanisms that
determine how large execution artifacts move between the active model context and durable task state.
Representative works are illustrated in Table 5.


_**3.2.1.**_ _**Working Memory**_


Working memory supports state maintenance along the current coding-task trajectory [181]. Its central
concern is not how much history to retain, but which pieces of information are most useful for the next action
under a limited context budget. In code agents, working memory often appears as structured prompt regions,
state summaries, failed-test records, file lists, or critical stack information. Its purpose is to mitigate context
explosion, reduce repeated localization, and preserve the local consistency of an ongoing repair or editing
trajectory [57, 182, 183, 45]. From a harness perspective, working memory is the active control surface
between the model and the code environment: it determines what the agent observes before choosing the next
tool call, edit, or verification step. Representative systems such as SWE-agent [57] and RepairAgent [183]
show that, even with the same underlying model, repository-level repair performance can vary substantially


<!-- source-page: 21 -->


Table 5: Representative memory and context management mechanisms for code-agent harnesses.


**Method** **Role** **Managed State** **Harness Operation** **Primary Use**


SWE-agent [57] Working Memory Repair trajectory; runtime Structured state track- Grounds repo repair in files, commands, and
state ing tests
CodeMem [45] Working Memory Context slots; edit state Budgeted slot manage- Stabilizes multi-step edits under context limits
ment

RepairAgent [183] Working Memory Bug evidence; tool outputs Dynamic prompt-state Carries evidence across autonomous cycles
updates


AutoCodeRover [46] Semantic Memory Repo structure; code evi- Structure-aware re- Grounds localization and patching in repo strucdence trieval ture
RepoCoder [47] Semantic Memory Retrieved repo context; Iterative repo retrieval Expands evidence for context-aware generation
snippets

CodeRAG [187] Semantic Memory Repo knowledge; code Querying; multi-path Selects repo knowledge for long-context compaths retrieval; reranking pletion


MemGovern [48] Experiential Memory Trajectories; reflections; Governed experience Reuses quality experience while filtering noise
critiques replay

ExpeL [189] Experiential Memory Reflection traces; learned Reflection replay Reuses reflections as task-solving strategies
lessons


MemCoder [190] Long-term Memory Commits; root causes; vali- Structured memory; Learns repo-specific intent-to-code mappings
dated fixes self-internalization

TALM [191] Long-term Memory Task histories; reasoning Vector retrieval; consol- Reuses past episodes for tree-structured generatraces; validated code idation tion


MIRIX [192] Multi-agent Memory Cross-agent state; interac- Cross-agent memory Routes shared memory across specialized roles
tion history routing

ChatDev [193] Multi-agent Memory Dialogue history; software Phase-level context Maintains context across role-based phases
artifacts passing


LongCodeZip [194] Context Compaction Long code context; repo Coarse-to-fine compres- Compresses code while preserving reasoning
snippets sion cues
SWE-Pruner [195] Context Compaction Interaction context; sur- Task-aware pruning Removes irrelevant context before agent decirounding code sions
SWEZZE [196] Context Compaction Issue context; fix ingredi- Lightweight learned Distills compact, fix-relevant evidence
ents compression


depending on how interaction state and execution feedback are organized. CodeMem [45] similarly treats
context as a managed resource, using budgeted memory slots to stabilize multi-step edits.


_**3.2.2.**_ _**Semantic Memory**_


Semantic memory provides task-relevant external evidence for the current coding process [184, 175]. In
code-agent settings, such evidence is usually repository-specific and program-structured, including class
definitions, function implementations, call relations, configuration files, documentation, issue descriptions,
dependency metadata, and historical implementation patterns. Semantic memory therefore transforms the
external codebase into a queryable evidence space that the harness can retrieve from and inject into the active
context [46, 185, 186, 187, 188]. Representative works such as AutoCodeRover [46] and RepoCoder [47]
show that repository-level coding tasks benefit not simply from retrieving more content, but from retrieving
evidence aligned with program structure. Mechanisms such as AST-based structured chunking, iterative
query rewriting, and retrieval strategies conditioned on current localization clues can substantially improve
the utility of retrieved context for downstream generation. In this sense, semantic memory turns the codebase
into a structured evidence layer for the current decision process.


<!-- source-page: 22 -->


_**3.2.3.**_ _**Experiential Memory**_


As code agents move from single-task completion toward continual repair and cross-project generalization,
increasing attention has been paid to experiential or episodic memory [197, 198]. Unlike working memory,
which maintains the current trajectory, or semantic memory, which retrieves repository evidence, experiential
memory captures reusable experience accumulated across tasks, such as repair trajectories, failure cases,
debugging records, and higher-level strategy patterns [189, 199, 200]. Its main value lies in enabling
cross-task transfer. Through mechanisms such as experience cards, reflection buffers, and record-and-replay
pipelines, a system can convert past successful or failed debugging processes into reusable units for future
problem solving [199, 48, 201]. Works such as MemGovern [48] further suggest that the quality of stored
experience matters more than its scale. Ungoverned historical records can introduce semantic noise, error
propagation, and false retrievals, whereas curated and quality-controlled experiential memory is more likely
to become a useful asset for repository-level repair.


_**3.2.4.**_ _**Long-Term Memory**_


When coding trajectories become longer, working memory and semantic memory alone are insufficient,
because the system must also cope with memory growth, compression-induced evidence distortion, and longterm drift. This makes long-term retrieval planning and memory control an increasingly important research
direction [202, 203, 204, 205, 206]. The focus therefore shifts from memory capacity to memory governance.
Representative systems such as MemGPT [207] and MemoryOS [208] move the discussion from what to store
toward when to write, when to compress, when to retrieve, and how to avoid contamination. Recent codecentric studies further ground this line of work in software engineering workflows. MemCoder [190] leverages
structured historical commits and human-validated solutions as persistent memory, enabling repositoryspecific experience accumulation over time. TALM [191] incorporates long-term memory into multi-agent
code generation, retrieving prior problem–solution traces and consolidating overlapping memories to control
redundancy. These works suggest that, for code agents, long-term memory should not simply accumulate
more history, but preserve validated and reusable experience in a compact and controllable form. Otherwise,
memory may shift from a resource for long-horizon software engineering into a burden that amplifies noise,
staleness, and error.


_**3.2.5.**_ _**Multi-Agent Memory**_


Multi-agent memory extends state management from an individual agent to a shared harness. From a systems
perspective, memory in code generation has a strong collaborative dimension [209, 210]. In multi-agent
frameworks, memory is not only a container for individual state, but also a medium for information sharing,
intention passing, and consistency maintenance across specialized roles [211]. Representative works such
as AgentCoder [50], MapCoder [44], MIRIX [192], ChatDev [193], and G-Memory [211] illustrate how
memory supports multi-agent planning, testing, reviewing, and trajectory coordination. In this setting, the
central challenge is no longer only retrieving relevant content, but controlling the granularity of sharing,
preventing information flooding, and supporting bidirectional access between high-level decisions and finegrained execution traces [210]. Accordingly, memory in multi-agent code generation increasingly resembles
a shared blackboard or collaborative state graph rather than a purely individual storage unit [212, 213].


_**3.2.6.**_ _**Context Compaction and State Offloading**_


Context compaction and state offloading are cross-cutting context-engineering mechanisms for memory
in code-agent harnesses [214]. Their goal is not to define another memory category, but to control the


<!-- source-page: 23 -->


boundary between active model context and durable task state. Long-horizon software engineering workflows
continuously generate high-volume artifacts, such as build logs, execution traces, repository diffs, test outputs,
and intermediate plans. Directly placing these artifacts into the prompt can quickly overload the context
window, amplify noise, and obscure decision-relevant evidence. A harness must therefore decide which
observations should remain in the active context, which should be compacted into concise summaries, and
which should be offloaded to external storage with retrievable handles [178]. Context compaction compresses
long interaction histories and massive tool outputs into structured, provenance-preserving summaries. For
example, a failing-test report can be reduced to the failing test name, key stack frames, suspected files,
and links to the full log [196, 215, 194, 195]. State offloading complements this process by preserving
full-fidelity artifacts outside the active window, such as in files, databases, trace stores, or protocol-style
resource interfaces such as MCP-style servers. The agent then receives compact summaries and resource
identifiers rather than raw logs or traces. By separating decision-relevant context from durable evidence,
context compaction and state offloading make memory more scalable, auditable, and compatible with
execution-time verification.


_**Discussion:**_ Memory in code-as-agent-harness systems can be understood as a unified state-management
layer that connects context management, repository evidence retrieval, experiential transfer, long-term
control, and multi-agent synchronization. Rather than being a single data structure, an enlarged context
window, or simply a vector database, memory coordinates where task-relevant state should reside and
how it should be reused throughout long-horizon software engineering workflows. Working memory keeps
the next action grounded; semantic memory exposes repository evidence; experiential memory supports
cross-task transfer; long-term memory preserves validated knowledge; and multi-agent memory synchronizes
shared state across roles. Context compaction and state offloading further extend this layer by separating
decision-relevant active context from durable full-fidelity artifacts, making memory more scalable, auditable,
and compatible with execution-time verification. Importantly, memory research in code agents cannot
be separated from _evaluation reliability_ . Many conclusions about memory gains depend on the quality of
evaluation pipelines [216, 217]: if tests are insufficient, log parsing is flawed, or benchmarks suffer from
memorization and contamination, then reported improvements may not reflect robust long-horizon behavior.
Looking forward, the key challenge is not merely to enlarge memory capacity, but to build higher-quality
write gates, structurally aligned retrieval keys, provenance-preserving compaction mechanisms, reliable state
offloading protocols, and rigorous evaluation paradigms that measure whether memory truly helps agents
remain grounded, consistent, and verifiable over extended trajectories.


**3.3.** **Tool Use for Agent Harness**


Tool usage is the action and observation layer of the code-agent harness. Once code is placed inside the agent
loop, the model must not only generate text, but also search repositories, edit code, execute tests, call APIs,
query documentation, and verify intermediate results [218, 219]. Tools therefore expand the agent’s action
space while also exposing external feedback signals that make the harness executable and inspectable. From
the perspective of code as agent harness, tool use is not merely an auxiliary capability for code generation. It
is a governed interface between model intent and external systems. A reliable harness must decide which
tools are available, how their schemas are exposed, what permissions each tool receives, where execution
happens, how results are sanitized or compacted, and when risky actions require human approval. Recent
agent SDKs and software-agent platforms make this shift explicit by packaging tools, sessions, guardrails,
handoffs, workspaces, and execution environments into reusable harness components [58, 220, 221]. In
parallel, sandboxed execution environments, including containerized or microVM-based workspaces, isolate
agent actions from the host system and make code execution more reproducible and auditable [22, 222, 223].


<!-- source-page: 24 -->


**Figure** 7: Overview of tool-using mechanisms for agent harnesses.


This harness-level view also highlights the importance of **tool lifecycle control** . Before a tool is executed,
the harness may apply permission checks, policy rules, argument validation, or human-in-the-loop gates.
After execution, the harness may sanitize outputs, summarize large logs, offload traces to durable storage,
update memory, or trigger verification tools. Lifecycle hooks make these control points explicit. They turn
tool use from a raw model-selected action into a monitored transition in the agent’s execution loop.


Existing work on tool usage for code agents can therefore be organized according to the primary harness
function that tools serve: (1) _function-oriented tool use_, (2) _environment-interaction tool use_, (3) _verification-_
_driven tool use_, and (4) _workflow-orchestration tool use_ . Function-oriented tools ground the agent in APIs,
libraries, and external documentation. Environment-interaction tools allow the agent to act inside repositories,
terminals, IDEs, browsers, and sandboxes. Verification-driven tools provide deterministic feedback through
tests, linters, type checkers, static analyzers, and runtime errors. Workflow-orchestration tools coordinate
multiple tools, roles, memory updates, and lifecycle policies into a reliable long-horizon execution process.
Representative works are illustrated in Table 6.


_**3.3.1.**_ _**Function-Oriented Tool Use**_


This line of work uses tools primarily to fill gaps in the model’s programming knowledge, especially APIs,
libraries, documentation, and external coding utilities [19, 224, 225, 227, 228, 229]. ToolCoder [19],
for example, starts from a clear bottleneck: code models often hallucinate APIs, choose inappropriate
functions, or fail on public and private libraries with sparse training coverage. To address this problem, it
integrates API search tools into the code generation process and trains models to decide when to query
the tool and how to select APIs from retrieved results. The key contribution is therefore not better syntax
generation alone, but better knowledge acquisition and API grounding. More broadly, retrieval-oriented
methods reduce dependence on parametric memory and make code generation more adaptable to long-tail
APIs, private libraries, and continuously evolving software ecosystems [225, 230]. They are most effective
when the main bottleneck is that the model lacks reliable knowledge of which function, API, or library
construct should be used. Accordingly, the core design challenges lie in query formulation, result selection,
evidence compression, and robust injection of retrieved knowledge into downstream generation. These
agentic methods are particularly suitable for API-oriented generation, library migration, and private SDK


<!-- source-page: 25 -->


Table 6: Representative tool-use mechanisms for code-agent harnesses.


**Method** **Role** **Tool Boundary** **Harness Operation** **Primary Use**


ToolCoder [19] Function-oriented API search tools API selection via trigger Grounds generation in retrieved APIs
prediction

CodeQA [224] Function-oriented API/doc query tools Tool-augmented API QA Retrieves API evidence for coding
RAG-for-Code [225] Function-oriented Repo, docs, API Retrieval-augmented context Knowledge for long-tail libraries


CodeAgent [185] Environment-interaction Repo files, tests Repo navigation, editing, Repo-level coding via environment
validation interaction
SWE-agent [57] Environment-interaction Shell, editor, repo, tests Agent–computer interface loop Resolves GitHub issues via shell
commands


AgentCoder [50] Verification-driven Test generation Programmer–tester–executor Refines code via generated tests
loop

VeriGuard [226] Verification-driven Execution, tests, verifier Verifier-guided tool loop Gates and repairs code via
verification


ToolNet [49] Workflow-orchestration APIs, tools, execution Learned multi-tool policy Routes tool invocations across
routing workflows
MapCoder [44] Workflow-orchestration Coding agents Multi-agent tool-supported Coordinates planning, generation,
workflow debugging
OpenHands [58] Workflow-orchestration Workspace, terminal, Unified software-agent Long-horizon tasks via reusable
browser, files, runtime workspace interfaces


usage, but retrieval alone is often insufficient when tasks require cross-file understanding and reasoning,
runtime debugging, or repository-wide dependency analysis.


_**3.3.2.**_ _**Environment-Interaction Tool Use**_


Unlike function-oriented tools, environment-interaction approaches treat tools as the interface through which
an agent acts inside the software engineering environment [231, 232, 233, 234]. Their central problem is
no longer only to obtain missing functions, but to operate effectively over repositories, development artifacts,
and execution environments. CodeAgent [185] shows that real-world repository-level code generation is
not simply about completing a single function from a prompt. Instead, the model must locate relevant
files, understand dependencies, inspect documentation, implement modifications, and validate outcomes
through testing. To support this process, CodeAgent integrates programming tools and agent strategies
for information retrieval, code-symbol navigation, code implementation, and test interaction over real
repositories. SWE-agent [57] pushes this idea further by formalizing the agent-computer interface, where
shell commands, file editing, and test execution become the primary interaction channel. RepairAgent [183]
similarly equips the agent with repair-specific tools for reading code, searching repair ingredients, applying
patches, and running tests. Together, these methods define the core trajectory of environment-interaction tool
use, which is especially relevant for repository-level generation, issue resolution, and open-ended software
engineering tasks.


_**3.3.3.**_ _**Verification-Driven Tool Use**_


A third line of work uses tools primarily for post-generation verification and iterative improvement. Verificationdriven tool use treats external tools as deterministic sensors for the harness. Compared with function-oriented
and environment-interaction tools, these approaches do not necessarily emphasize external retrieval or broad
repository navigation. Instead, they use tests, execution results, compiler errors, runtime traces, type checkers,
static analyzers, and verifier feedback as the main signals for improving code quality [226, 235, 236, 237].


<!-- source-page: 26 -->


AgentCoder [50], for example, uses a programmer agent, a test designer agent, and a test executor agent to
form a closed loop of code generation, test construction, execution, and refinement. In this paradigm, the
central role of tools is verification rather than retrieval. From the code-as-agent-harness view, verification tools
make agent progress inspectable: test failures, stack traces, coverage gaps, type errors, and static-analysis
warnings become structured observations that update working memory and guide the next action. The key
design issue is how to route these observations back into the loop [226]. Since raw logs may be too long
or noisy for the active context, the harness should parse, summarize, and offload verification traces while
preserving full-fidelity artifacts for audit and replay.


_**3.3.4.**_ _**Workflow-Orchestration Tool Use**_


Workflow-orchestration tool use focuses on how multiple tools, roles, and control policies are organized into
a coherent agent workflow [238, 239, 240, 241]. In long-horizon software tasks, the agent may need to
retrieve evidence, localize bugs, modify files, run tests, inspect failures, update memory, ask for approval,
and repeat this cycle several times. The challenge is not simply adding more tools, but deciding when each
tool should be invoked, with what permissions, under which context, and how its result should update the
harness state [49]. Recent agent SDKs and software-agent platforms make this orchestration layer explicit by
packaging typed tool schemas, session state, workspaces, guardrails, handoffs, tracing, and human-review
mechanisms into reusable harness components. Lifecycle hooks further refine this boundary: pre-use hooks
can validate arguments, enforce permission policies, or block risky commands, while post-use hooks can
sanitize outputs, compact logs, update memory, or trigger follow-up verification. Representative systems such
as MapCoder [44] exemplify workflow orchestration by assigning agents to example recall, planning, code
generation, and debugging, thereby decomposing a difficult coding problem into coordinated subproblems.
CodeAgent [185] also studies how tool calls should be scheduled and structured in repository-level workflows.
This class is particularly important for long-horizon code agents, where realistic software tasks require
demand decomposition, context selection, candidate exploration, execution-based verification, and final
repair under explicit control policies [49, 242].


_**Discussion**_ : Tool usage in code agents has evolved from isolated API retrieval to a full harness mechanism
for action, observation, verification, and governance. Function-oriented tools ground implementation choices
in external knowledge; environment-interaction tools allow agents to act over repositories and execution
environments; verification-driven tools provide deterministic feedback; and workflow-orchestration tools
coordinate these capabilities through SDKs, sandboxes, guardrails, and lifecycle hooks. The core challenge
is no longer whether a model can call a tool, but whether the harness can make tool use safe, auditable,
and useful for long-horizon execution. Future code-agent harnesses should support typed tool schemas,
permission-aware invocation, sandboxed execution, lifecycle hooks, result sanitization, context compaction,
state offloading, and reproducible traces. These mechanisms ensure that tools expand the agent’s action
space without sacrificing reliability, safety, or verifiability.


**3.4.** **Harness Control through the Plan, Execute, and Verify Loop**


Code-as-harness systems require a control loop that turns model intentions into bounded, observable, and
revisable state transitions. This subsection frames that loop as _Plan–Execute–Verify_ (PEV): the harness first
externalizes an intended change and its validation criteria, then executes the change inside a sandboxed
and permissioned environment, and finally verifies the resulting state through deterministic sensors and
human-review gates. This framing unifies planning, execution, debugging, verification, and escalation as
parts of a single harness-level control process.


<!-- source-page: 27 -->
fail through syntax errors, runtime exceptions, incorrect outputs, incomplete edge-case handling, unsafe
operations, or violations of project-specific conventions, making one-pass generation insufficient [243].
Recent systems revise code through feedback from compilers, runtimes, tests, static analyzers, humans,
and auxiliary agents [244, 245, 246, 23]. From the harness perspective, this process can be reframed as a
_Plan–Execute–Verify_ (PEV) loop: the agent externalizes an intended trajectory, executes bounded actions
inside a controlled environment, and verifies the resulting state before the next transition. The growing
engineering ecosystem around agent harnesses reinforces this view: recent curated resources distinguish
orchestration, working state, execution substrates, evaluation harnesses, observability, and governance as
separable harness layers rather than incidental implementation details [247, 248, 249, 25].


In this view, the harness acts as a _cybernetic governor_ : a control layer that observes the effects of agent actions
and regulates subsequent state transitions. Rather than merely forwarding error messages to the model, it
observes the repository and execution environment through deterministic sensors such as linters, parsers,
compilers, type checkers, unit tests, integration tests, static analyzers, fuzzers, runtime monitors, and CI
pipelines. These sensors turn a coding trajectory into inspectable signals, including pass/fail outcomes,
diagnostics, failing traces, coverage gaps, security warnings, resource limits, and policy violations. The
harness can then decide whether to continue execution, revise a patch, request more context, route the task
to another module, reduce permissions, or escalate to a human reviewer. Table 7 summarizes this control
surface; the remainder of this subsection follows the loop from contract formation, through sandboxed state
transition, to deterministic verification and evidence-grounded repair.


<!-- source-page: 28 -->


Table 7: Representative methods and systems for PEV-loop harness control.


**Method** **PEV Role** **Core Mechanism** **Signals and Gates**


CodePlan [42] Plan, structural Dependency plan graph Repo links, critiques
MapCoder [44] Plan, orchestration Map-code-test stages Handoffs, tests, failures
OpenHands [250] Full PEV harness Stateful edit-exec workspace Diffs, logs, tests, approvals
SWE-agent [57] Execute, CLI Replayable shell interface Commands, patches, tests
Daytona [251] Execute, cloud sandbox Isolated dev workspace Files, limits, snapshots
E2B [252] Execute, code-browser sandbox Cloud code-browser sandbox Stdout, limits, UI state
Self-Debugging [243] Verify, self-debug Explanation-guided repair Errors, tests
Reflexion [244] Verify, reflection memory Verbal feedback memory Outcomes, critiques
Debug Like a Human [245] Verify, stepwise debug Runtime-step checks Traces, variables, asserts
Iterative Refinement [246] Plan–Verify feedback Project-context repair Compiler diagnostics
QualityFlow [253] Verify, quality gate Quality feedback routing Tests, success, stopping
AgentCoder [50] Verify, multi-agent repair Coder-tester-executor loop Tests, failures, critique
AutoSafeCoder [52] Verify, safety sensors Static checks, fuzzing Alerts, traces, tests
VeriGuard [226] Verify, verified gen. Verifier guard layer Proofs, tests, alerts
LiteLLM [254] Permission gateway Proxy policy routing Approvals, denials, cost logs


_**3.4.2.**_ _**Planning as Contract Formation**_


The planning phase turns a user request into an explicit contract over the next state transition. A robust plan
does more than decompose the request into implementation steps; it also identifies relevant files, expected
invariants, validation commands, rollback points, and risky operations. This makes planning a harness
artifact rather than an unobserved reasoning trace. In repository-level tasks, such artifacts constrain the
subsequent action space by specifying which components may be read, which files may be edited, and
which verification criteria must be satisfied before completion [40, 42, 44]. Repository-local instructions and
tool protocols strengthen this contract layer: AGENTS.md-style guidance, MCP server registries, typed tool
schemas, adapters, and protocol gateways make the available actions inspectable before execution rather
than discovered opportunistically during execution [255, 256, 257, 258, 259, 260, 261, 262]. The PEV
framing also clarifies why planning and debugging should not be separated: failed verification updates the
plan, while the plan determines which verification evidence is meaningful.


_**3.4.3.**_ _**Sandboxed Execution and Permissioned State Transition**_


The execution phase realizes the plan as a bounded and observable state transition. The sandboxed environment is the operational substrate of the loop: it provides an isolated filesystem, dependency state, shell,
language runtime, browser or IDE interface, and resource boundary in which agent-generated actions can be
run without directly compromising the host system [263, 22]. Contemporary execution-substrate work is best
read as functional clusters rather than as an undifferentiated catalog. Coding sandboxes expose filesystems,
Git operations, shells, package managers, and code-execution backends [251, 252, 264, 265, 266, 250];
computer-use substrates add browser, desktop, LSP, or IDE state [267, 268, 269, 270, 271]; and durable
runtimes emphasize microVM or WASM isolation, snapshots, warm pools, resumable sessions, benchmark
environments, and always-on operating contexts [272, 273, 274, 275, 276, 277, 278]. Sandboxes also
improve reproducibility because the harness can replay the same patch, command, seed, dependency lockfile,
or test configuration under comparable conditions. Without this stable substrate, verification signals become


<!-- source-page: 29 -->


difficult to interpret, and failures may reflect environment drift rather than program defects [250, 217, 279].


Execution must also be permissioned. A multi-tier model separates low-risk observation from high-risk
action: a read-only tier supports repository browsing, retrieval, static inspection, and log analysis; a sandboxedit tier supports local patching, test execution, and temporary dependency installation inside an isolated
workspace; and a full-access tier covers network access, credentials, deployment commands, package
publishing, destructive filesystem operations, or Git history mutation. Actions in the final tier should be
guarded by mandatory human-in-the-loop (HITL) gates because their consequences can extend beyond the
sandbox. Recent software-agent systems and harness engineering work increasingly expose these control
points through explicit tools, sessions, policies, approval prompts, and audit logs [280, 250, 281, 178, 282,
283]. Gateway and policy layers then provide the production counterpart: systems for model routing,
tool registration, proxy-level logging, centralized guardrails, security automation, and falsifiable approval
evidence keep governance outside the prompt alone [254, 284, 285, 262, 286, 287, 288, 289, 290, 291].


_**3.4.4.**_ _**Verification through Deterministic Sensors**_


The verification phase closes and, when necessary, reopens the loop by comparing the new state against
explicit constraints. Compilation and static-analysis feedback provide low-cost sensors before full execution,
including parser diagnostics, type errors, lint warnings, and security alerts [246, 292, 293]. Runtime signals
expose failures that only arise along concrete execution paths, such as exceptions, assertion breaks, invalid
API usage, resource exhaustion, and timeouts [294, 295, 245]. Test-based feedback then evaluates whether
the observed behavior satisfies the intended specification, using unit tests, integration tests, regression
tests, fuzzing, or benchmark-specific evaluators [243, 296, 297, 298]. Evaluation harnesses broaden this
idea from a single test command to repeatable task distributions: they encode evaluator logic, simulation
hooks, red-team cases, or RL-style environments that can compare harness variants under controlled
conditions [299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309]. Compared with natural-language
critique, these sensors are deterministic or at least reproducible enough to serve as control signals. Human
or agentic critiques remain useful when failure evidence is sparse, but in a governed PEV loop they should
interpret sensor outputs rather than replace them [244, 310, 54].


Verification also supplies the evidence for repair, reflection, and termination, so these activities are treated
as consequences of the Verify phase rather than as an independent stage. When a check fails, the same
sensor evidence can determine whether the harness should ask the model to diagnose the failure, retrieve
missing context, regenerate a localized patch, route the task to a testing or security agent, or abandon
the current branch. Self-reflection mechanisms help transform raw diagnostics into actionable hypotheses,
such as whether the failure comes from incorrect control flow, missing edge cases, misunderstood APIs, or
inadequate tests [311, 166]. However, reflection is reliable only when it remains grounded in executable
evidence. Systems such as AgentCoder, AutoSafeCoder, and QualityFlow illustrate this principle by combining
agentic critique with independent execution, static analysis, fuzzing, or test-quality gates [50, 52, 253].
Termination should likewise be governed by verification rather than by model confidence: a loop can stop
when required checks pass, when additional attempts no longer improve the state, when the risk tier changes,
or when human review is required.


_**Discussion:**_ Recasting iterative debugging as the PEV loop emphasizes that reliability comes from governed
state transitions, not simply from better repair prompts. Planning externalizes intended changes and risk
assumptions; execution applies them inside sandboxed and permissioned environments; verification uses
deterministic sensors to decide whether the state is acceptable; and HITL gates preserve accountability when
the action space crosses a safety boundary. This framing unifies static analysis, runtime errors, tests, critique,


<!-- source-page: 30 -->
self-reflection, and human review as components of a cybernetic harness that regulates the agent’s trajectory
over executable program state.


**3.5.** **Agentic Harness Engineering for Adaptive Harness Optimization**


Agentic Harness Engineering (AHE) names a harness-level design problem: how to measure and revise the
software substrate that turns a language model into a coding agent. Whereas prompt engineering changes
instructions and context engineering changes what evidence is presented to the model, AHE treats the
operating environment itself as the object of analysis, including tool schemas, planning artifacts, memory
policies, retrieval strategies, sandbox configuration, verification sensors, permission tiers, routing rules, multiagent workflows, and human-review gates [281, 178]. This perspective is useful because many observed
failures in code agents arise from missing repository context, brittle tool interfaces, weak validators, excessive
token cost, poor retry policies, or mismatched permission boundaries rather than from model generation.


Existing work can be read as three complementary strands. AutoHarness studies automatic synthesis of code
harnesses [14]; Meta-Harness formulates harness design as an optimization problem over model-facing
infrastructure [13]; and observability-driven AHE emphasizes telemetry-rich diagnosis of where the agent
loop fails and which harness component should change [281]. Related work on reflective prompt evolution,
self-evolving workflows, and live software-engineering agents supports the same systems view: changing the
scaffold around the model can change agent behavior without retraining the base model [18, 312, 182].
Engineering guides from OpenAI, Anthropic, and LangChain converge on the same practical lesson: reliable
agents require explicit harness loops, tool contracts, trace replay, evaluation suites, context budgets, and
controlled execution boundaries [248, 249, 313, 314, 28].


_**3.5.1.**_ _**Deep Telemetry as the Optimization Substrate**_


The central substrate of AHE is _deep telemetry_ : structured traces that connect model decisions, harness actions,
environment states, and outcomes. A shallow log may record only the final answer or pass/fail result. Deep
telemetry records the decision process in greater detail: prompts and retrieved context, token usage and cost,
model/tool latency, tool arguments, permission requests, edited files, sandbox snapshots, command outputs,
test results, stack traces, lint warnings, branch decisions, rejected alternatives, human interventions, and final


<!-- source-page: 31 -->


task outcome. In code-centric settings, these traces are especially valuable because program execution already
exposes state transitions through logs, tests, diffs, and runtime behavior [128, 96, 37]. In production systems,
this role is increasingly served by observability and reliability stacks that record traces, metrics, prompts,
model traffic, eval results, and cost signals [315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327].
Evaluation, observability, and governance systems therefore provide complementary telemetry channels:
evaluators expose task-level regressions, tracing stacks expose trajectory-level causes, and policy gateways
expose boundary violations that an Evolution Agent can turn into harness revisions.


Telemetry turns harness revision from anecdotal debugging into comparative diagnosis. Token-cost traces
reveal when retrieval or reflection stages consume budget without improving verification outcomes. Decisiontree traces show where the agent repeatedly chooses unproductive tools, edits irrelevant files, or loops
between failed strategies. Failure traces cluster recurring patterns such as missing dependencies, weak
tests, hallucinated APIs, flaky sandboxes, over-permissive tool calls, or premature termination. Because
these signals are linked to concrete artifacts, they can be replayed and compared across harness versions,
making it possible to evaluate whether a change improves reliability rather than merely changing surface
behavior [216, 217].


_**3.5.2.**_ _**The Evolution Agent**_


An _Evolution Agent_ is a meta-level agent that uses deep telemetry to propose, evaluate, and promote revisions
to harness components. Unlike a task agent, which edits the target repository, the Evolution Agent edits the
operating conditions under which later task agents work. Its input is a corpus of trajectories; its output may
be a revised prompt template, a retrieval policy, a more precise tool schema, an added validator, a changed
permission rule, a workflow-topology adjustment, or a new regression test. This role is closely related to
self-evolving multi-agent systems in which specialized agents inspect execution logs, attribute failures to
workflow components, and update collaboration structures [328, 329]. In the harness setting, the same idea
is generalized from multi-agent topology to the control surface of the agent runtime.


A typical Evolution-Agent loop contains five stages. First, it _observes_ trajectories by collecting telemetry from
PEV executions. Second, it _diagnoses_ failure modes by attributing cost, latency, invalid actions, test failures,
or permission denials to specific harness components. Third, it _proposes_ candidate revisions, such as rewriting
tool descriptions, changing context packing rules, adding a linter, modifying retry limits, or inserting a HITL
gate before risky commands. Fourth, it _evaluates_ the revised harness on held-out tasks or replayed traces
using deterministic sensors and regression tests. Finally, it _promotes_ only changes that improve reliability, cost,
or safety without regressing previously solved cases. This keeps AHE within the same engineering discipline
as the PEV loop: proposed changes must be executed, verified, and made auditable before adoption.


_**3.5.3.**_ _**Governed Harness Mutation**_


AHE should not be confused with unconstrained self-modification. Because the Evolution Agent changes
the harness that controls later task agents, its actions require stronger governance than ordinary code
repair. Candidate harness changes should be evaluated inside sandboxes, compared against fixed regression
suites, and recorded with auditable rationales. Changes that alter permission boundaries, network access,
credential handling, deployment behavior, or human-review requirements should require HITL approval
before activation. In this sense, the Evolution Agent is itself subject to the PEV loop: it plans a harness
mutation, executes it in an isolated evaluation environment, verifies the result through telemetry and
regression tests, and escalates risky changes to humans.


_**Discussion:**_ Agentic Harness Engineering extends the code-as-harness view from operating agents to analyzing


<!-- source-page: 32 -->


Table 8: Representative methods for Agentic Harness Engineering with telemetry-driven revision targets.


**Method** **Category** **Telemetry** **Revision Target**


AutoHarness [14] Harness synthesis Failures, fixtures, assertions Harness code and tests
Meta-Harness [13] Harness search Code, scores, traces Prompts, tools, scripts
AHE [281] Telemetry-driven optimization Cost, decisions, latency, failures Context, tools, validators
GEPA [18] Reflective prompt evolution Scores, feedback, critiques Prompts and instructions
EvoMAC [328] Workflow topology evolution Handoffs, idle roles, loops Agent roles and graph
SEW [312] Self-evolving workflow Workflow scores, failures Stage order and roles
Live-SWE [182] Online agent evolution Live issue trajectories Policies, tools, memory
GroundedTTA [232] Test-time adaptation State-action evidence Adaptation rules
RLEF [104] Execution-feedback learning Execution rewards, failures Feedback reward signal
DeepEval [300] Evaluation harness Scenario and metric traces Regression suites, gates
FeedbackEval [23] Repair evaluation benchmark Feedback-task scores Failure taxonomy and eval set
Langfuse [315] Observability platform Spans, cost, latency, evals Dashboards and replay
OpenLLMetry [321] Trace instrumentation OpenTelemetry spans, calls Harness instrumentation
Promptfoo [299] Evaluation harness Scores, regressions, failures Eval gates and red tests
LiteLLM [254] Gateway governance Routing, budgets, failures Budgets, fallbacks, tiers


the infrastructure that operates them. Deep telemetry provides evidence for locating failures across prompts,
tools, memory, sandboxes, validators, permissions, and workflows. Evolution Agents use this evidence to
propose and evaluate harness mutations, turning harness design into an iterative and measurable engineering
process governed by verification and human approval.
