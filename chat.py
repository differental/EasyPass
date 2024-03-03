# import the OpenAI Python library for calling the OpenAI API
from openai import OpenAI
import os
import json 

from dotenv import load_dotenv
load_dotenv()

api_key = os.environ.get("OpenAI_API_key")

if api_key is None:
    raise ValueError("OpenAI_API_key is not set in the .env file")



client = OpenAI(api_key=api_key) 
msg = "Generate four mechanics problems that involves angular momentum and moment of inertia, only output the problem and nothing else. A spherical ball is rolling down the slope 10 degrees. The ball has a mass of 10 kg and a radius of 5 cm. The coefficient of friction is 0.2. Calculate the angular momentum and moment of inertia of the ball at the bottom of the slope. A cylinder with a mass of 20 kg and a radius of 10 cm is rotating about its vertical axis with an angular velocity of 10 rad/s. Calculate the angular momentum and moment of inertia of the cylinder. A disk with a mass of 15 kg and a radius of 12 cm is rotating about its horizontal axis with an angular velocity of 5 rad/s. Calculate the angular momentum and moment of inertia of the disk. A rectangular block with a mass of 25 kg and dimensions of 15 cm by 20 cm by 30 cm is rotating about its vertical axis with an angular velocity of 8 rad/s. Calculate the angular momentum and moment of inertia of the block."
samplemsg = "Generate four mechanics problems that involves angular momentum and moment of inertia, only output the problem and nothing else. A spherical ball is rolling down the slope 10 degrees. The ball has a mass of 10 kg and a radius of 5 cm. The coefficient of friction is 0.2. Calculate the angular momentum and moment of inertia of the ball at the bottom of the slope. A cylinder with a mass of 20 kg and a radius of 10 cm is rotating about its vertical axis with an angular velocity of 10 rad/s. Calculate the angular momentum and moment of inertia of the cylinder. A disk with a mass of 15 kg and a radius of 12 cm is rotating about its horizontal axis with an angular velocity of 5 rad/s. Calculate the angular momentum and moment of inertia of the disk. A rectangular block with a mass of 25 kg and dimensions of 15 cm by 20 cm by 30 cm is rotating about its vertical axis with an angular velocity of 8 rad/s. Calculate the angular momentum and moment of inertia of the block."

sampleresponse = r"""
\documentclass[a4paper, 12pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{graphicx}
\begin{document}
\section*{BEGIN OF PAPER}
\subsection*{Problem 1}

A spherical ball is rolling down the slope $10 degrees$. The ball has a mass of $10 kg$ and a radius of $5 cm$. The coefficient of friction is $0.2$. Calculate the angular momentum and moment of inertia of the ball at the bottom of the slope.

\subsection*{Problem 2}

A cylinder with a mass of $20 kg$ and a radius of $10 cm$ is rotating about its vertical axis with an angular velocity of $10 rad/s$. Calculate the angular momentum and moment of inertia of the cylinder.


\subsection*{Problem 3}

A disk with a mass of 15 kg and a radius of $12 cm$ is rotating about its horizontal axis with an angular velocity of $5 rad/s$. Calculate the angular momentum and moment of inertia of the disk

\subsection*{Problem 4}

A rectangular block with a mass of 25 kg and dimensions of $15 cm$ by $20 cm$ by $30 cm$ is rotating about its vertical axis with an angular velocity of $8 rad/s$. Calculate the angular momentum and moment of inertia of the block.

\section*{END OF PAPER}
\end{document}
"""

MODEL = "gpt-3.5-turbo"
response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant helping the user compile a text-based problem into a full LaTeX source code"},
        {"role": "user", "content": "Turn the following problems into a LaTeX document:\n" + samplemsg},
        {"role": "assistant", "content": sampleresponse},      
        {"role": "user", "content": "Turn the following problems into a LaTeX document:\n" + msg},
    ],
    temperature=0,
)

print(response.choices[0].message.content)

#print(json.dumps(json.loads(response.model_dump_json()), indent=4))
