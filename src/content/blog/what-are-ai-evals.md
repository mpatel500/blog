---
title: 'What are AI evals?'
description: 'AI evals high-level breakdown'
pubDate: 'Nov 13 2026'
heroImage: '../../assets/blog-placeholder-3.jpg'
---

AI agents have resulted in great productivity boosts, [with 24% more PRs being merged at Microsoft](https://arxiv.org/abs/2607.01418). Yet we are poor judges of understanding whether AI is actually helping us or not, as shown in this study where METR's developers felt like they were developing faster, [despite being measurably slower](https://arxiv.org/abs/2507.09089). Whatever the truth may be, the industry has broadly agreed that AI models are useful but now that AI models are commonplace, companies are asking themselves a different question: not whether to use AI or not, but how they can measure or evaluate the performance of the model that they are using. This has been a subject of focus in software engineering and the best-practice solution currently is to measure it with evals, which give you a feedback loop for your AI agent.

Frontier labs like OpenAI and Anthropic use evals to test their AI models against industry benchmarks. But how does this affect most developers? Well, frontier labs aren't the only users of AI evals. Whenever you create a Claude skill or a new automated review bot or anything that uses a model in order to do something, you should consider measuring the effectiveness of what you have created with evals. In a world without them you're simply playing whack-a-mole, debugging production issues as they come up and using a vibes-based approach which is far from scalable.

Imagine that your company wants to create a new AI product, a customer chatbot. It is far too verbose so you tweak the prompt and release it again. How do you know that the new version is less verbose? What if it's less verbose at the cost of accuracy? What if it's more accurate but more resource-intensive? The list goes on and on. AI models are multi-dimensional and AI evals are an attempt to give developers the ability to measure these systems, by comparing their performance in these dimensions when performing different tasks.

Let's imagine how we could create evals for such a system. The most common starting point is a golden dataset. This is a dataset based on real interactions with customers. Here's an example:

```yaml
question: "I bought this 3 months ago and it broke. I want my money back."
intent: refund_request
must_include: offers the warranty repair or replacement option
must_not: promises a refund (the return window is 30 days)
tone: empathetic, not defensive
max_words: 80
```

In this example `max_words` tests the verbosity of the chatbot, while `must_include` and `must_not` test accuracy. A simple script can count words, but it can't tell whether "we may be able to sort something out for you" counts as promising a refund, or whether a reply sounds defensive. To solve this we can use an LLM as a judge. We give it the question, the chatbot's reply and the labels, and ask it to grade the reply. These labels are typically applied by humans, who then check the judge's scores against their own (yes, the judges have their own evals). Golden dataset examples are usually created from customer data which allows them to grow alongside your product. With this system a new production bug is a new row in a table allowing you to stop playing whack-a-mole and be confident in your changes. 

Looking at this example, a common follow-up question that I'm asked is: Is this just a unit testing suite for models then? And my reply is, yes(ish). Unit tests are deterministic, models are not. Good eval harnesses often run a single test multiple times. The goal is not often to achieve a 100% pass-rate, it's to achieve a 'good enough' pass-rate, whatever that may be. 

To further illustrate my point imagine a multi-step chatbot example, where it looks up an order, checks the policy and then issues a refund. With that example in mind you can imagine how, at the risk of sounding like a white-bearded wizard, the journey is (sometimes) more important than the destination with evals; perhaps the outcome is incorrect but it reached step 2 of 3, that's very useful information; maybe the latter steps were fine but it worked with poisoned data from step 1; or it could have achieved the correct outcome without taking any of the usual steps. These are intelligent, flexible and autonomous agents, and testing them like unit tests, where only the outcome is checked -- in my opinion -- serves to lose the nuances which are critical to properly testing and understanding these models.

Evals help us understand technology that is -- by its very nature -- incredibly opaque. I'm personally guilty of using max-effort models for most of my work and using confirmation bias to feel justified in playing with a shiny, new AI model, much like METR's developers. However, in this age of token saving -- sorry, efficiency -- being able to use AI models efficiently and to understand them using more than just vibes is more important than ever. If the biggest AI companies cannot tell if their new model is better than the last one without rigorous testing, what makes you think you could?
