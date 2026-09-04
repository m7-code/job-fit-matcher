from langgraph.graph import StateGraph, END
from state import ResumeJDState

from nodes.parse_resume import parse_resume
from nodes.parse_jd import parse_jd
from nodes.extract_resume_entities import extract_resume_entities
from nodes.extract_jd_entities import extract_jd_entities
from nodes.semantic_match import semantic_match
from nodes.score_and_explain import score_and_explain


# Step 1: Graph banao, State ka blueprint do
graph = StateGraph(ResumeJDState)

# Step 2: Har node ko naam de kar graph mein add karo
graph.add_node("parse_resume", parse_resume)
graph.add_node("parse_jd", parse_jd)
graph.add_node("extract_resume_entities", extract_resume_entities)
graph.add_node("extract_jd_entities", extract_jd_entities)
graph.add_node("semantic_match", semantic_match)
graph.add_node("score_and_explain", score_and_explain)

# Step 3: Batao pehla node kaunsa chalega
graph.set_entry_point("parse_resume")

# Step 4: Edges — batao kis node ke baad kaunsa node chalega
graph.add_edge("parse_resume", "parse_jd")
graph.add_edge("parse_jd", "extract_resume_entities")
graph.add_edge("extract_resume_entities", "extract_jd_entities")
graph.add_edge("extract_jd_entities", "semantic_match")
graph.add_edge("semantic_match", "score_and_explain")
graph.add_edge("score_and_explain", END)

# Step 5: Graph ko "run karne layak" banao
app = graph.compile()