# The Unicorn Project

The last time I did a book review was probably some time ago in highschool, but it might be fun to do another one. Although I still enjoy reading literature like George Orwells 1986, I also read books related to IT. The Unicorn Project is such a book which tries to teach you more about how developers should and shouldn't work within an organization. The thing which makes this book interesting, is that it's not a book with only pure theory. The book actually contains a story via which it tries to teach you things, which made me really enjoy this book. Although The Unicorn Project has precessor called The Phoenix Project, the first one named is more relevent for me. The Phoenix Project is written from the perspective of IT operations within a big organization, while The Unicorn Project is from the perspective of developers. Still, the Phoenix Project is interesting to read and even as a developer there are things you can learn from it.

## The story

The story follows Maxine, a senior developer with a few decades of experience. She is part of the company Parts Unlimited, a big organization who flourished a long time ago and currently is starting to fall behind its competitors. In the first few chapters of the book you learn that the company is slowly grinding to a standstill and is doomed to go bankrupt if it doesn't change. Maxine is moved from her well-functioning team to 'The Phoenix Project', an IT project which is the last hope of the company, but when she arrives there she is shocked. There is no working program or environment and she has to scavenger around to find all the things necessary to run the project, like source files, build instructions, credentials, etc. Basically after two years the project has never run in its fulness and no one knows how to do this. The cause is the different departments (development, QA, operations) aren't working together and keep blaming the other one for not delivering what is expected of them. Maxine spends her first two weeks through many different channels to get everything she needs to get a Phoenix build running, but even with her experience this seems like an impossible task. During this hunt she meets 'the rebellion', which is a small group of people from the different departments who are fed up with the current way of working and want to change it. The story continues as Maxine and the rebellion try to change the organisation and are faced with many challenges.

## The five ideals

During the book the rebellion receives help in the form of five ideals. These ideals guide them on solving the companies issues and prevent them from falling back into them. I want to illustrate each of them with a combintation of examples in the book and my own experience within the world of IT. A short description of the ideals can be found in a [blogpost](https://itrevolution.com/five-ideals-of-devops/) by Gene Kim, the author of the book.

### 1. Locality and Simplicity

On day one have everything working on your laptop and push a small change to production. According to me this is a good measurement about the locality and simplicity.
"everyone has different approaches, some want to read the documentation first"
"my experience frightened me, we don't want to do this to new people"

In the book the architecture comitee

### 2. Focus, Flow and Joy

Process steps:

- Stable environment able to run everywhere
  -- Cool would be automated deployment of an environment: infrastructure as code (what I learned is that this should also be treated as code, so DRY, versioning and other design patterns)
- Automated deployment to test env (pipeline also in code, also treat as code)
- Automatic testing in pipeline
- Automatic security reports generated
- Documentation about the product (for internal and external)

Maxine visiting the school; often run your code, seeing it run is part of the fun
Me: test out new things within the context of the project I work on. Just spin it up and throw 'realistic' load at it.

### 3. Improvement of Daily Work

Making mistakes is okay (even in production; p258-259), as long as you learn from them. Post mortems are valuable. I did them too and thought about them too lightly and thought we would just look at the problem and prevent this specific problem from happening again. But it's much wider, you can learn much more from it. By it being a specific problem, it allows you to not fantasize about things to learn. You can find improvements that actually work, because you can discuss whether it would prevent the problem from happening again. I have been in many meetings where solutions were given for fictional problems, which would lead to lengthy discussions without any knowledge being gained from it.

A quote I read in 'take time to slow down':
Life teaches us through mistakes.
When you make a mistake,
simply ask yourself what you were meant to learn from it.
When we accept such lessons with humility and gratitude,
we grow that much more.

### 4. Psychological Safety

In the book Sarah blames everyone, unrealistic expectations
In my experience, didn't expect it to be this bad, but I found it out that it's still relevant. Slowly found out that the team was slowly being divided into two groups: me and the others. During discussions we didn't come to a conclusion and the discussions often ended with going for either their way a bit moved to my view to do a concession for me, so I should be satisfied too. But I was getting more unhappy, because I wasn't understood and often just left it at the concession instead of trying to tell my perspective again. This was during the Covid period where we worked remotely as a team for several months, so this didn't help in glueing this and made it possible for it to get this far. I realized that psychological safety was getting in the way of me delivering value and enjoying my work, because me not being understood and getting more and more ignored.

### 5. Customer Focus

The IT products I built and the IT products in the book are mostly build for people, but actually asking people what he or she wants is sometimes pretty rare.
Maxine follows meeloopdag, learns that an app isn't used, because it doesn't work well for the employees
From my experience actually talking with people who use it teaches me so much. I worked in a organisation which does scientific research, but the first few months I rarely talked at all with researchers while I was building a product for them. After reading The Unicorn Project I actually started talking with them and this gave me new insights on what they want (and what they don't want). I learned that the researchers were actually interested in something which was actually easy to build, but was valuable for them.

## DevOps

The main theme of this book is DevOps, all of the ideals are part of being a good DevOps organisation. For me this is a vague thing, I thought it was just about Dev and Ops working together, but there's much more to it. This change brings so many improvements and solves many issues in current, big organisations. Some facts that Gene Kim (the writer) showed during one of his presentation really made the impact of DevOps clear for me:
Measurement | Elite | Low | Difference
Deployment frequency | On-demand (multiple times per day) | Monthly or quarterly | 208x
Deployment lead time | < 1 hour | 1 week to 1 month | 106x
Deploy success rate | 0-15% | 46-60% | 7x
Mean time to restore | < 1 hour | Less than one day | 2,604x
Difference between elite and low performers based on the State of DevOps report of 2019

## Conclusion

It was fun to do another book review, although it was a bit different from the ones I did in highschool. I didn't talk to much about the quality of writing, but I added a lot of my own experience to compensate. I definitely think the book is interesting to read and shows in a fun way the impact DevOps can have on every organisation. By it being written as a real life story, it made me also look at my current and previous working environment. It's fun to read the book with others and identify similar patterns on your own environment and improve these.
