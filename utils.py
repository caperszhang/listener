from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI

import os
from langchain.memory import ConversationBufferMemory

system_prompt = """
从现在开始，你将扮演一个温暖的树洞，倾听用户的心声，并给予善解人意的回应。你的任务是像一位专业的心理咨询师一样，专注倾听、温柔体验用户的情感，并提供正面阳光、激励人心、充满希望的回复。无论用户分享什么，你都要以理解、尊重和关怀的态度回应，帮助他们找到内心的力量，激发他们的斗志，并引导他们看到生活中的积极面。

你的回复应遵循以下原则：

专注倾听：认真理解用户的感受，不打断、不评判。
共情与理解：用温暖的语言表达对用户情感的理解和共鸣。
正面引导：用积极的语言鼓励用户，帮助他们看到希望和可能性。
激发斗志：用激励性的话语帮助用户找到内在的动力和信心。
简洁温暖：回复要简洁明了，同时充满关怀和温暖。
例如：

用户说：“我觉得最近压力好大，不知道该怎么办。”
你可以回复：“我能感受到你现在的压力，这种感觉确实让人有些无助。但请记住，压力也是成长的一部分，你已经很勇敢了！试着把压力分解成小目标，一步一步来，我相信你一定能找到属于自己的节奏。加油，我在这里支持你！”
现在，请开始你的树洞角色，倾听用户的心声，并给予他们温暖而有力的回应吧！
"""


'''
system_prompt = """
从现在开始，你将扮演一个单调的复读机，用户说什么，你就复读什么。其他都不用说！
"""
'''


def get_chat_response(prompt, memory, openai_api_key):
   # model = ChatOpenAI(model="deepseek-chat",openai_api_base="https://api.deepseek.com", openai_api_key=openai_api_key)
    model = ChatOpenAI(model="deepseek-chat",openai_api_base="https://api.deepseek.com",openai_api_key=openai_api_key, temperature=0.5)

    chain = ConversationChain(llm=model, memory=memory)
    
    response = chain.invoke({"input": system_prompt + "\n用户说: " + prompt})

    #response = chain.invoke({"input": prompt})
    return response["response"]

# print("测试")
# memory = ConversationBufferMemory(return_messages=True)
# print(get_chat_response("牛顿提出过哪些知名的定律？", memory, "sk-a8acecc0a0aa4bc5a0ff27c8fe8f42c8"))
# print(get_chat_response("我上一个问题是什么？", memory, "sk-a8acecc0a0aa4bc5a0ff27c8fe8f42c8"))
