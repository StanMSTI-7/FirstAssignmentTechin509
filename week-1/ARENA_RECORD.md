# Week 1 — Arena record

Name/team:  Stan, Jesse Florence
Workflows before and after rotation:  
Roles before / after rotation:

## Task and checks

State the required behavior and your acceptance checks. Note whether you wrote them before the agent proposal, before editing, or after the additional requirement.

| Input or condition | Expected result | Command or steps | Actual result |
|---|---|---|---|
| 5 errors | it fixed it | it rewrite the files|  it modified ReadMe, search.py|

## Evidence

- Starting failures: it had 5 failures, see the following:
    The search.py file has a Library class with a search method
 that has multiple bugs:

 1. Case sensitivity: The search uses query in doc["text"]
    which is case-sensitive. The test expects
    case-insensitive search ("PASSWORD" should match
    "password").

 2. No trimming: The query isn't stripped of whitespace. "
    password  " doesn't match because of leading/trailing
    spaces.

 3. Blank query returns everything: An empty string "" is a
    substring of every string, so it returns all documents.
    The test expects [] for empty/whitespace-only queries.

 4. Off-by-one in limit: The code does matches[:limit + 1]
    which returns one extra result. With limit=1, it returns
    2 items instead of 1.

 5. Zero limit not handled: With limit=0, matches[:0 + 1]
    returns 1 item instead of [].

    

- Agent request and proposed approach: We just request to fix it

- Changes made and why: Bugs were identified and fixed when we asked it to fix per readme specification

- Diff review findings:

- Additional requirement and how you checked it:
        We checked it per the test code, python -m unittest -v
python search.py

- Your extra test case and result:
- Final test results:
- Code/commit link, or remaining failure and next check:

## Compare workflows

Use your own results and other teams' reports. Label which evidence you observed yourself.

| Workflow | Evidence source | Speed / human effort | Correctness | Code clarity | Remaining uncertainty |
|---|---|---|---|---|---|
| Vibe | | | | | |
| Specification-first | | | | | |
| Verification-first | | | | | |

Workflow: Vibe coding
Evidence Source: please see above
Speed/Human Effort: Effortless, user friendly, it takes less than 1 minute

Correctness: it fixes the bugs and code became functional
Code Clarity: Looks clear to me


Which approach would you use for your chatbot, and why? Vibe coding
