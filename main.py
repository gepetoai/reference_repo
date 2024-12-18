from gepeto import Gepeto, Agent

gepeto = Gepeto() #takes local env variable GEPETO_API_KEY
agent = Agent("escalator")

agent.run()