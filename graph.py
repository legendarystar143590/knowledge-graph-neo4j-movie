from langchain_community.graphs import Neo4jGraph
import streamlit as st

# Use the correct Neo4j URI format and credentials
graph = Neo4jGraph(
    url=st.secrets["NEO4J_URI"],
    username=st.secrets["NEO4J_USERNAME"],
    password=st.secrets["NEO4J_PASSWORD"],
    database="neo4j",  # specify your database name if different
)