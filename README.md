# Easy Pass

## Inspiration

As university engineers, we often find ourselves running out of past papers when preparing for exams and tests. Therefore we decided to develop an AI bot that generates maths and physics problems tailored to the users needs.

## What it does

Generates maths and physics problems in a particular topic for students to train themselves and revise.

## How we built it

By training a pretrained model zephyr-7b-beta with existing university maths and physics problems with PyTorch and AutoTrain, we find out models generating decent quality maths and physics problems according to the topics we ask for. We then utilise a chatgpt api to format the problems and formulas into LaTeX, where it gets turned into beautiful printable PDF.

## Challenges we ran into

Resource limits imposed by AutoTrain, PyTorch are extremely frustrating. We didn't want to use a worse model, so we had to find ways to change environments and try to make it work on azure, where we have more resources available.

## Accomplishments that we're proud of

We managed to successfully run our model at 1am, after almost 12 hours of work on the same issue.

## What we learned

Training AI models, quantization

## What's next for EasyPass

Introduce a web interface for user to upload their own test papers, which are then combined with our own database to produce more tailored questions


