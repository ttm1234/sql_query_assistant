from langchain import OpenAI, SQLDatabase
from langchain.agents import create_sql_agent, AgentType
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.chat_models import ChatOpenAI
import _base

_base.patch()


# db_url = "mysql+pymysql://root:abc12345@127.0.0.1/clx_act_cook?charset=utf8mb4"
db_url = 'mysql+pymysql://user1:user1passwordAAAA@116.205.143.247/goods_search?charset=utf8mb4'


def main():
    db = SQLDatabase.from_uri(db_url)
    toolkit = SQLDatabaseToolkit(db=db, llm=OpenAI(temperature=0))

    # 跑一次0.78元
    # agent_executor = create_sql_agent(
    #     llm=OpenAI(temperature=0),
    #     toolkit=toolkit,
    #     verbose=True,
    #     agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    # )

    # 跑一次0.05元
    agent_executor = create_sql_agent(
        llm=ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613"),
        toolkit=toolkit,
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS
    )

    question = '''
    sku 表有多少行
        
    '''.strip()
    r = agent_executor.run(question)
    print(type(r), r)


if __name__ == '__main__':
    main()
