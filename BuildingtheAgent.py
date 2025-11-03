# Building the Agent

# Finally, we create an agent that leverages the SQL engine tool. We use the CodeAgent class from smolagents, which writes actions in code and can iterate on previous output according to the ReAct framework:

from smolagents import CodeAgent, HfApiModel
agent = CodeAgent(
   tools=[sql_engine],
   model=HfApiModel("meta-llama/Meta-Llama-3-8B-Instruct"),
)
# Run the agent with a natural language query
agent.run("Can you give me the name of the client who got the most expensive receipt?")
