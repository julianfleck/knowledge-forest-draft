MinSpecs for the Knowledge Forest experiment - April 16
VIEW RECORDING - 131 mins (No highlights): 

---

0:00 - Corey Gouker
  From what I could tell, nobody's there yet. Like I asked, you know, three different AI models, like what's the current state of the art, if you combine CRGTs and end-to-end encryption and local first, and it pointed to, what is it, any type as an option, right?  So it doesn't really have a clear idea of what we're even talking about. And as far as the actual ecosystem goes, it looks like there's too many trade-offs.  And so people are, they're doing like non-multiplayer, which is doable. But then as soon as you get into the multiplayer side, you have issues with the key rotation and how to handle that with multiplayer.  And I'm not really sure, like, from what I could tell, I think where you're currently at would probably be, like, I think you're well positioned to address the visualization side of things, like actually doing good mapping of all the data and representing it in a usable way versus, hey, this is just a obsidian graph that you can look at.  In and out on. And that's about that. Right. But you can imagine, instead of having just basic backlinks where you're just, you know, clicking through, instead, you're zooming in and out of those backlinks in a 2D or 3D space.  And as you zoom in, you're switching context to whatever you're zooming in on. When you zoom out or clicking out, you're switching to a different context.  So it might be, you know, a usable spreadsheet in one area, but then just the actual, you know, pretty page in another.  But doing that in a way where you're transitioning from 2D to 3D and back is the real challenge, right?  Because you want to be able to navigate a space in the same sort of way you would navigate your memory palace, right?  Where you're kind of just connecting the dots internally, if you're, you know, the type of visualizer that does that.  But at the same time, you, there's people that don't do that and don't want that. They just want an index and be able to click through.

3:02 - Julian Fleck
  I feel like coming back to the different layers that you identified there, I feel like there are a bunch of different pieces on the table and I think we just need to carefully decide which of these to address and in what constellation do we want to address those.  My trajectory working on these things was like I was coming from the interface side, right? So I was trying to build experiences.  Then I realized I'm missing the data structures behind the experiences that feed the experiences. So I switched focus and worked on that.  And now the whole identity and storage layer that you're Like that's like an even deeper layer of that one.  So I feel like what I'm building with Recurse is the like, or is a representation layer for knowledge units, like atomic knowledge units that you want.  If you want so that you can compose into like, I don't know, different layers of abstraction and that you can use to feed such experiences.  And then below that, you have the identity layer and you have the question of like, where do you want to actually store that?  I had a conversation with Tim, who Christina also threw into this group. And yeah, it's, it's interesting that, that he's, um, that they're working on this like missing piece if you want.  So, so it's, um, I talked a bit about what I'm doing. He talked a bit about what he's doing.  it's really like there is very little overlap, but they integrate very well.

5:12 - Christina Bowen (SocialRoots)
  complimentary, yeah.

5:13 - Julian Fleck
  Exactly.

5:14 - Christina Bowen (SocialRoots)
  And I really like Tim's attitude in terms of he's very determined not to let extraction happen. He's super aligned on the just basic principled side, as far as I can tell.  Yeah.

5:30 - Julian Fleck
  But he also seems very eager to build something that is a bit more applicable on top of what he's offering or what he's able to offer right now.  Because the case he's making for his technology, that's very much catering towards people who want traceability and accountability and audit signals in the end.  And it's like very dry territory that doesn't really enable that much. But if you pair that with, like, the sensemaking layer on top of it, and potentially even, like, an interface layer that allows you to navigate and access all this, then suddenly you're looking at something that's a bit more, like, tangible in a way.  So with Tim, it's just, I'm just saying that because I think he is, like, he has some of these things solved, right?  Like, he has some of the, like, this entire identity and, like, trust layer is, like, that could be what he has.  I've been working extensively on the, like, I don't data structure itself somehow that would just, like, interface with the identity provider.  And, like, up to a level where, like, every piece of information on the graph could be having it. It's own identity, you know, and like have its own like granular like access controls that gets like get to decide how things propagate through the graph and stuff like that.  So that's one thing that we just wanted to look into, like how how feasible is it to take those two things that we have right now and integrate them somehow.  And then this interface thing is the thing I'm most like interested in. And I think that's the most like that's the fun part of all of this.

7:38 - Christina Bowen (SocialRoots)
  I know, right?

7:39 - Julian Fleck
  All the finished work.

7:40 - Christina Bowen (SocialRoots)
  Yeah, this is what you want to build.

7:43 - Julian Fleck
  This is like I have a bunch of stuff in my drawers also, like the stuff that I've been working on in that regard.  But I feel like we're not there yet. Like we're not even at the point where it makes sense to think about this.  Like, we know the primitives that we built into these systems. And we know that we will be able to, like, synthesize over a subset of the graph.  And that enables something like semantic zooming, right? So we know where we can go from there. But I'm kind of, I'm just kind of wary of, like, I don't know, getting entangled in this, like, sphere for now.

8:30 - Christina Bowen (SocialRoots)
  Putting the trim on the windows before the window has a frame?

8:32 - Julian Fleck
  Yeah, yeah, yeah.

8:35 - Corey Gouker
  Like, even though that's, like, I really want to do this.

8:38 - Julian Fleck
  Like, for years, I'm like, I want to be at the point where I can pick up these work streams again to get there.

8:44 - Christina Bowen (SocialRoots)
  But my feeling is just we're not there yet. It seems like the experiment, Corey, that you and I talked about doing just to test the 60 minimum viable context.  And adding that in to Julian's understanding of frame semantics and how to apply that might be a generative place to talk today.  Because that's like, what can we do? Well, that was the, let's see if I share screen, will this work?

9:25 - Corey Gouker
  And I try, my real core focus is always security. And I more and more kind of have to avoid that, or at least I feel like I do.  Because it ends up feeling like a giant rabbit hole. Well, it's a giant rabbit hole, but it's also a thing that forces people to pause and wait.  And that kind of can feel like a negative thing for a lot of people. Because I don't think anybody has any...  Real clue about how to actually solve some of the real issues, like, for example, just being able to pick up a phone and record a video, and, you know, there goes your entire thing around identity and security, and, you know, so it's, it's, the human layer is yet to be solved in any, like, any domain around security.
  SCREEN SHARING: Christina started screen sharing - WATCH: https://fathom.video/calls/640382150?timestamp=602.266567

10:27 - Christina Bowen (SocialRoots)
  Okay, let's put security and identity and stuff aside. We have, we have, yeah, have that people, we have the Coasis people, we have Tim in the mix.  They're all talking about that. And you're in those conversations, Corey. So I think, for me, I really want to get like, what can we test now?  Like, if this is, God, how do I zoom in on here?

10:52 - Corey Gouker
  Command plus.

10:53 - Julian Fleck
  Yeah, I think it's command plus.

10:58 - Christina Bowen (SocialRoots)
  Great. Okay, that's better. So if we have this idea that contextualizing knowledge sharing with a light, minimal subset of contextual data, I'll fix that later, but can that actually produce an event log that is showing learning happening rather than just kind of a useless event log that you would find in Slack or Discord or something?  And this would not be a UX or UI test, but an experiment in whether the event log, if we log this stuff together, would actually help.  And this is the beginning of what I'm thinking about. Capturing, like, who is giving the link, who's receiving the link, which might be a, it's always going to be a person sharing, maybe within a context.  And it might be either a group of people or a person receiving it, depending on if it's a DM or a shared space.  And then, like, what kind of content is it? What are the tags? Are they just sharing a thought? Is this a sort of mature document?  Is this a finished product that they're sharing just for knowledge sharing? And then what is the context and how?  So I think that if we think about, like, what can we do with a lightweight experiment? at this minute.  Let's Thank Just to capture, like, Corey, you remember we were talking about just like a very simple form that we'd ask everybody to fill out five minutes at the end of the day, fill out at least one thing you learned from somebody else, and fill these fields out, and have that populate the actual content and wrapper of context in Markdown files, and that that would be sort of a good first test.  Does that make sense?

13:44 - Julian Fleck
  I think that question went to Corey.

13:49 - Christina Bowen (SocialRoots)
  Corey, do you remember this?

13:55 - Corey Gouker
  Yeah, we didn't get into the discussion about, like... Where and how that would live, I think.

14:03 - Christina Bowen (SocialRoots)
  I think we were just going to do a GitHub repo that doesn't have any intimacy gradients yet. It's just like whoever's doing the experiment has access to the pile of markdown files.  So we don't have to actually have any kind of intimacy gradients. We can just say they shared this with us and it doesn't matter.  If Josh shares something with me in a DM and Signal, I can log it at the end of the day and put it in the team thing.  It's not like there's a high enough trust in this pile of nerds that we don't have to keep DMs and DMs, etc.  And we're not going to log anything that's sensitive anyway. So I think that the implementation of just having a pile of markdown files on a private GitHub repo would be fine.

15:00 - Corey Gouker
  Yeah, and this is where the Discord bot, some of the existing work that Josh has done might come in handy as far as capturing that instead of having a form.

15:17 - Christina Bowen (SocialRoots)
  Manual, yeah. So let's go into the TL draw together. And I have this blank page that I made for us right now.  But if we go up to that, where it says Knowledge Forest MVP Experiment, that dropdown menu, you can go to MVP Unflattenable Data.  And this was sort of Corey and I talking through the details. I'll get more clear on that. I wanted to start by talking through how I'm thinking of this happening, and then we can go over to the blank slate and look at what the experiment will require, and the architecture for that, and whether or not we're using the questions we have for Josh and GuildBot and all of that, and then Julian, what you already have that might serve or not.

16:32 - Julian Fleck
  One question before we jump into that. You keep saying links, so like the unit of information that we're looking at is like a link to something?

16:44 - Christina Bowen (SocialRoots)
  I mean, it could be a link. It also could be just a thing I want to put it. It could be a block in a markdown kind of thing where you're...  Like,-pasting, you know, something out of a Signal DM or whatever and saying, like, this was useful for my thinking in this way and for this reason.  So I'm really trying to get away from the knowledge as the graph and the nouns and the existence of knowledge as if we know everything and into, like, what is that process of knowing?  And can the frame and can the can the minimum viable context from the IDM metaphysics plus frame semantics help us actually get to where the knowledge graph is a secondary thing on which knowing happens together?

17:41 - Julian Fleck
  Does that make sense?

17:43 - Christina Bowen (SocialRoots)
  That makes sense.

17:44 - Julian Fleck
  Yeah.

17:45 - Christina Bowen (SocialRoots)
  Okay. So if you come up over here, you see where my cursor is here. There's, you know, the... Let's just say like a seeker membrane could be, it doesn't have to be a directional, like it might be the, like I reach out to you and I ask you for something, then you give me a link.  So I'll have to get clear on the language, the seeker and the sought, but basically like either a group or a person or maybe an agent, but not for this experiment, has an existing knowledge garden.  We each have a private repo of our own stuff, and then we can say, hey, this thing that, you know, maybe, I don't know, there's a bit, it's.  A few people have shared Christopher Alexander's stuff lately and Josh hasn't read it. So he would say like, hey, three people have shared a pattern language, these particular pages for this particular reason with regard to 3D visualization and what implications a pattern language has for augmented reality and like finding stuff in your mind palace kind of thing.

19:30 - Julian Fleck
  Knowing that Josh is interested in that or knowing that the like sharing entity, like where was it getting the context from?

19:48 - Christina Bowen (SocialRoots)
  So probably from the conversation around wherever the link is shared.

19:54 - Julian Fleck
  Got it.

19:55 - Christina Bowen (SocialRoots)
  So maybe we center conversations in a Discord. channel for the length of the experiment if we're using the guild bot and that gets working in Discord.  don't know. But then...

20:10 - Corey Gouker
  is a little bit iffy, I think. We definitely need to get more dialed in on it, as well as the type of content that is shared.

20:22 - Julian Fleck
  Yeah.

20:24 - Christina Bowen (SocialRoots)
  Content shared is usually either somebody typing something and having an insight.

20:27 - Corey Gouker
  What I mean, though, is, is it an image? Is it a video? Is it audio? Is it a text file?

20:35 - Christina Bowen (SocialRoots)
  Right? That's sort of why I say link. Because usually image, video, your Christina, you can't just say link.

20:41 - Corey Gouker
  It's really, like, if I just have a link and I pull out a screenshot of that, you know, there's also the entire, you know, abstract syntax tree.  There's all the markdown that might go with that. There's, you know, it might have a video embedded. I downloading the...  Am I doing a transcript of that video? There's so much. It's like the possibility space when you just say link is quite expansive.

21:12 - Christina Bowen (SocialRoots)
  I think you would only pull whatever would come up in the metadata for the link preview. We wouldn't pull on everything.  That's part of how a graph could turn into relevance cultivation. If the aim is relevance realization and this practice of not getting interrupted in flow, I don't want to dump a link in my knowledge garden and then be presented with a whole semantic tree of the transcript.  I just want to know that I want to watch it later. And it's not until I watch it that that kind of depth is needed.  So think of it in the lightest way. Think of, Corey, think of the KnowledgeGarden tool that you were describing when we were mapping it out with regard to the fractal protocol.

22:12 - Corey Gouker
  Yeah, I mean, and it's still quite the challenge because, like, if I just share an image, right, there still needs to be some kind of analysis on that image.  You know, like, I can't just use the, there may not be, like, exit data if it's not a photo and it's just a screenshot, right?  It might just be, say, screenshot and a date timestamp, right? But it doesn't necessarily give you the to get the data, let's put that aside for just a second.

22:47 - Christina Bowen (SocialRoots)
  And let me walk through what I'm thinking here so Julian knows it. And then we'll flip over to a clear use case in the blank slate and, like, map that out.  Okay? So. Somebody shares something with somebody else or somebody else's. There's a shared record created that has six dimensions, putting aside how you get those six dimensions for a minute.  But this shared record, if, you know, in this experiment, everybody's going to have permission to share with everybody else.  So we're just ignoring the permission. And then that accepts the relevant content. In this case, there's nothing that would be rejected anyway.  So, you know, the link or image or whatever goes into my knowledge garden. And that record informs. Where I'm putting, like, it keeps the context with it.  So however we get these six dimensions is kept in wherever I put it in the knowledge graph. And that helps that context stay there while I can wrap it in further context.  So if I share it with the group, but then I want a private note about it in my personal knowledge graph, I can further wrap it and say, this was shared with the group.  You know, Corey gave this link, shared it with the group. It has group relevance over here and these six dimensions that are relevant for the group.  But then I can put it in mine and wrap it in further and say, this is what it means to me and how I'm going to take it forward in my own investigations or knowledge tree.  And then the hope is that... The individual and the event and the meaning of the thing, the sort of inclusion, proximity, and meaning, which is the three axes, will actually result in breaking flow less often.  And when, I mean, I run into this all the time right now, like I have a whole bunch of tabs that I left open because I'm not done with them for whatever reason.  And then I have to go back and read the page again and not, I don't remember why I left them open or any of that.  Or, you know, if I do, I have to think about it. And that itself breaks flow. So, cool. So with that, let's flip over to the other, the blank slate, and then just say what might happen as a use case in those two weeks.

26:19 - Julian Fleck
  Let's maybe talk about the context for a bit. Because from what I hear, there is, so if we have this resource here, so I translate link as resource now and we can talk about what that means in detail later.  But if there's a resource, there is context attached to the resource itself. But then there is also context in regard to the recipient, or like plural recipients.  So that creates It's basically like, I don't know, let's say we treat this group of three people as the group of recipients and Christina shares a resource that would create like two different interpretations of the original contextualization of that resource in regards to Corey's and mine personal knowledge garden.  Is that correct? Okay. That kind of breaks the context is attached to the resource paradigm a bit already.

27:45 - Christina Bowen (SocialRoots)
  Context is not attached to the resource.

27:47 - Julian Fleck
  Okay. Then I misunderstood that.

27:51 - Christina Bowen (SocialRoots)
  It's a wrapper when I'm looking at it from a particular context. So if I'm looking at it in my knowledge garden.  Got it. Got it. That's why you call it a context membrane also.

28:06 - Julian Fleck
  Okay. Understood.

28:08 - Christina Bowen (SocialRoots)
  That makes sense.

28:10 - Julian Fleck
  It's like an image.

28:10 - Corey Gouker
  might just be a JSON file with the context that, you know, that's tied to that particular image, right? Like, if you have extracted the exit data, you might have additional, like, context in there, right?  It might just be a sidecar file that lives with it.

28:27 - Julian Fleck
  Yep. In regards to the viewer, like, it's a view translation that we're looking at. So it's like, if I'm looking at the resource, the context is different from when Corey is looking at the resource.

28:43 - Christina Bowen (SocialRoots)
  Well, we need a shared reality too, right? Like you, if I share a resource with you and Corey, all three of us should see why I shared that.  So they should see this. Context that I shared it in and any meaning that we can get. The why field is the one I think we are going to need people to slow down and write.

29:09 - Julian Fleck
  Yeah. But the why field would relate to a group, right? Like I'm trying, I'm just trying, that's why I'm asking.

29:18 - Christina Bowen (SocialRoots)
  a one-on-one.

29:18 - Julian Fleck
  a one-on-one.

29:20 - Christina Bowen (SocialRoots)
  Yeah.

29:21 - Julian Fleck
  There's still a why if I'm sharing it with me.

29:23 - Christina Bowen (SocialRoots)
  I mean, there's also a why when I share it in my own knowledge graph, when I position it.

29:29 - Julian Fleck
  Exactly. And I'm just, I'm just sensing that there is like, there are different ways to model this. And I think we should be like sort of intentional or like, at least we should know why we model it in that way and what that entails, you know, like, you know, if you have the scenario where you have one-to-many plus one-to-one, like as an additional scenario.  You basically have these like transclusions of the original content wrapped in different contextual wrappers that would need to be provided somehow.  if you're coming from, okay, like Christina is sharing something and she fills out the why, then who does this why relate to?  You know, like does the why relate to the group? Yeah, the why relates to the group. And an individual, and if it relates to the group, how can we, like, how can we get from the, like, rather wide framing of the group to the stuff that's probably most interesting for anyone using this, which is, how does it relate to me personally?  You know, like, how can it fit into what I already know?

30:53 - Christina Bowen (SocialRoots)
  Yeah.

30:54 - Julian Fleck
  And that's like, that's the hard problem also that we're trying to solve and why all this, like, I don't know, ZK knowledge stuff.  It's interesting. It's like we want to have a mechanism that mediates between different entities without having to reveal all of the, like, personal knowledge of that entity, you know, like the tap into your personal knowledge garden and say this is relevant for you because X.  So I think, again, like, we need to be clear about, like, what happens if the resource gets dropped into the system?  Like, how, like, is it one context object that appears or is it multiple that appear in relation to everyone's, like, personal knowledge space?

31:44 - Corey Gouker
  Also, like, is it a human that's doing the instantiation of the, you know, six things or is it a human, right, if it's agent or human there?

31:58 - Julian Fleck
  Correct.

32:00 - Corey Gouker
  And just thinking about the zero knowledge scenario, you know, how and what are you really yelling into the cave, you know, and how does that change the actual security position of that?  I mean, because if you're providing certain contexts to a group, yeah, I mean, you're trying to provide some sort of gradient on the six dimensions in some ways, but not in others.  Because you could just be talking about the resource, and then some of the six dimensions aren't fully provided with the resource when you share it to some people, but they are with others.  So there's different scenarios there. The one I come back to, though, is like agent versus human, who's filling this out?  Because there are trade-offs, if you have a human doing it, may not, that needs to be part of like the actual, you don't want to break the flow there.  But if you have an agent doing it, then it may not do it properly. And there's...

34:00 - Julian Fleck
  Yeah, but what is properly also?

34:02 - Corey Gouker
  Well, just thinking about asking about my original thing, like when I was saying, okay, well, we have multiplayer, we have end-to-end encryption, local first, CRDTs.  Is there anything doing that? It's like any type.

34:17 - Christina Bowen (SocialRoots)
  doesn't really understand the language ecosystem. For a two-week experiment. Like, all I'm trying to do is test whether or not the hex event frame is useful.

34:30 - Julian Fleck
  I'm not trying to deal with ZK proofs.

34:33 - Christina Bowen (SocialRoots)
  I'm not trying to deal with local first. I'm like, identity on GitHub, a big repo we all share. Let's test how we contextualize things.  So can we scope the, like, is that important for how we design the experiment?

34:48 - Julian Fleck
  Or can we scope it in and not go down security rabbit holes? I think the interesting aspect for me is, like...  Like, Like, Like, Like, Like, Like, Like, Like, Picking up Corey's, like, what you shouted into the cave, it's a bit like, for me, it's more like, I want to, like, be able to throw stuff at a wall and see what sticks.  But also, we want to have a mechanism that makes stuff stickier for the participants in that group. So if I throw something at Christina's wall, I want it to be stickier for her.  By contextualizing it in a way that makes more sense to you when you receive that piece of information.

35:41 - Christina Bowen (SocialRoots)
  Yeah, but that doesn't have to come from how you contextualize it from yourself. It could come from the act of sharing.  If I take the time to add a link, I can usually add a sentence of why I'm adding it.  Everything else probably can be gotten.

35:57 - Julian Fleck
  I understand. I understand. It's just what I'm saying is... And what I think is interesting to think about, at least, like I'm not saying we need to make this part of the MVP scope, but what's interesting to think about is there is a potential for, because I have a shallow understanding of your thinking, right?  And I think we talked a lot, and I think we're aligned on a lot of things, but I still don't really trust the depth of my understanding of your thinking, if you want so, right?

36:33 - Christina Bowen (SocialRoots)
  Yeah, no, we have a lot to do there, yeah.

36:36 - Julian Fleck
  We have the potential to develop something that strengthens that by having access to some of our personal insights. So the way I see this experiment is also like, we kind of need to talk about what does the personal knowledge garden look like?  You know, what lives there? Like, how do we seed that before we even start to run? And then do we want to make use of some kind of mediator, or do we want to develop a mechanism that mediates between the people sharing stuff there?  Because I think it's interesting. If there is a potential agent that can tap into my personal knowledge base and can say, hey, the material that Corey just shared is relevant to you in these three ways, that kind of takes the responsibility from Corey to sit there and think hard about why that might be interesting for me.  And I think that's the friction point that we see all the time right now, because it's like you either drop something into the Telegram group, like just some random link, and you have to.  Make the context surrounding that link so general that it applies to everyone seeing this. Or you just, I don't know, like completely hijack the conversation by pulling two people in there and saying, hey, this is relevant for you because of why, you know.

38:18 - Christina Bowen (SocialRoots)
  But then it might be interesting to everybody else and they can contextualize it for themselves. It doesn't matter. You can add people in a conversation.  Working out loud, that is a pattern, right? Hey, this is relevant. I'm saying it to Josh, but I'm putting it in the Atlas Research Group because I want people to know that we're talking about it.

38:40 - Julian Fleck
  They don't have to do anything with it.

38:42 - Christina Bowen (SocialRoots)
  So, okay. Does that make sense, Corey?

38:49 - Corey Gouker
  Yeah, but also there's the time aspect. And... And... And... And... And... And... And... And... And... And... And... Thank It takes time to decide and figure out whether or not something's contextually relevant or not, even in just a conversation where it's like, okay, you sent something to Josh.

39:11 - Christina Bowen (SocialRoots)
  You can still just drop links too, right? You don't have to. You can create. Something has to provide the context.

39:21 - Corey Gouker
  If I provide five links and say, okay, this is part of this conversation, I still have to read the conversation.  I still have to potentially open five different links to decide if any one of those is relevant. It's either that or I trust an agent to help me with the process.

39:45 - Christina Bowen (SocialRoots)
  Yeah. But also if I drop five links, because I'm a rabbit hole generator and I don't take the time to provide context, maybe that's like.  Your agent will deprioritize that because I didn't aim it at you. I didn't do anything to contextualize it or say why I was sharing it in this group.  I'm just like in a Telegram group and I drop a bunch of links. And you can look at the little preview and choose whether or not to go down that rabbit hole or not.  And if you have an agent helping you with that, great. That's out of the scope for me. I don't care what your agent does at this point.  I just want to know if I do take the time to contextualize it, which if I didn't would just be an empty slot in the frame.  But at least the frame would still have that I shared it in this context and at this time. And it was like a published public thing on the Internet or it was a document or it was, you know, a thought.  And it doesn't matter if all. If the six dimensions are filled out, that will actually give it like, hey, somebody really contextualized this and it might be important to look at.  Or, you know, somebody just shared this rabbit hole and you can go down it or not if your attention and inclination, like just how we do right now, right?  You know, you see raw links in the map makers space all the time. People just drop them and they don't even say why.

41:25 - Corey Gouker
  Yeah, I mean, I just saw Simon respond to himself and signal with the Instagram thing. And I have no clue because I can't read the preview and I'm not going to click on the Instagram.

41:36 - Christina Bowen (SocialRoots)
  exactly.

41:39 - Corey Gouker
  But that is a good example, though, right? Like what we're talking about, like there might actually be context in there that is totally relevant.  And it's just a question of whether or not, you know, I take the time or some agent takes the time to, you know, provide that, you know, potential relevance.

42:01 - Christina Bowen (SocialRoots)
  Yeah. And so this is an experiment is if we take the time to provide that relevance to each other, does, and we take the time to, at the end of the day, because we don't have the full system built yet, say, these are three things where somebody taking the time to provide relevance was meaningful to me.  I learned something. I took the time to dive down a rabbit hole, add it to my knowledge garden in this way.  So there's like the sharing events where somebody shares the resource, but then there's also the, okay, I took that and I took action on it.  But you never know.

42:42 - Corey Gouker
  Yeah. makes me wish there was some existing standard of sharing beyond just a URL, right? Where encoded in there is the additional information.  And this is what you kind of get with advertising. That's what the UTM stuff is all about.

43:06 - Christina Bowen (SocialRoots)
  And people don't even, you know, that's, that's what I think that frame semantics gives us.

43:13 - Corey Gouker
  Well, no, what I'm saying is human, like, so if like that Instagram link, right, there's, if you look at it, there's like a, you know, a question mark, and it has like, all the tracking .  Yeah, yeah, all the tracking .

43:29 - Julian Fleck
  Right.

43:30 - Corey Gouker
  That's the machine tracking  that we've done. For machines, but at a human level, it doesn't have any of the six dimensions.  Right.

43:38 - Christina Bowen (SocialRoots)
  And for humans, that means actually writing something out and it does, it has the who one, it has, it has the, if you had access to Instagram, and you could read the data, which is a membrane question.  It does have some of the data. It has the what because you can do semantic search. It has. It's who won, who originated it, who made the post.  It probably has the Instagram context of Simon grabbed it and shared the link. So it has sort of the who won within Simon is sharing this to our group.  So it has some of it, but it doesn't have all of it. There's a lot of empty slots. And that's sort of what I want to do.  I want to say, if we take the time for two weeks to fill out the slots for at least one to five things that we find every day, what does that do to our learning?

44:38 - Corey Gouker
  At the end of the day, what I'm trying to say is at the end of the day, it's too late, right?  And this is why it would be just fantastic if it was built into the way we share stuff on the fly.

44:56 - Christina Bowen (SocialRoots)
  So, yes, it would be fantastic. I think it should be on the fly. Can we do an experiment before we build the whole thing that we just commit to?  I know the end of the day is too late, but I'm going to tell you three things I knew I learned today as a team to see if this hex event record, which the group would have a whole string of these things.  Each of our personal knowledge resources would have a whole string of these things about how we got it, where we contextualized it, where we touched it next, where we touched it next.  The whole event log is like a chain within each context, and if it's a shared context, we can all see this, but if it's a personal context, I'm just putting a wrapper around it that's my personal context.  And maybe when I look at that, I can see like six chains where I shared this in this group and it has a long chain, I shared this in this group and nobody picked it up.  And I contextualized it myself because it's a core text. But it's like, before we build the whole thing, I just want to do a tiny experiment to see if the dimensions are right.  I feel like you're trying to build the whole thing. But maybe that's just to understand it.

46:17 - Julian Fleck
  I just keep thinking, I'm not sure which of those two routes is actually quicker to build. Or which carries more friction, if you want so.  You know, like the problem I see here is really on the user side, like on the participant side. Like having the time and headspace and intentionality to first of all identify why it would be relevant to share this and that.  And then contextualizing it. them doing that... that... I'll see you Like as a routine, essentially, versus we build something that tries to approximate this and tries to automate this.  then our job is to review how well it worked and we learned something from that. I'm just not sure which of those is more likely to yield results.  Because I know myself, like I suck at this. Like sometimes I zone out and I'm like, I'm not going to click on any links for a week.  Like not doing it. Like I have enough stuff.

47:30 - Christina Bowen (SocialRoots)
  If you had an agreement with 10 people that you would do that for two weeks, you would probably do that.

47:37 - Julian Fleck
  And I'm willing to be the annoying, hey, do your thing at the end of the day for everybody.

47:43 - Christina Bowen (SocialRoots)
  And it doesn't matter if we had a bunch of links that were not contextualized. Like all I want to know at the end of the day is did you actually go down any rabbit hole and like add it to your personal knowledge garden?  That's it. So we could do it the lightweight way if it's... It's more helpful to think through what we would build if we're actually building it.  I'm fine with that. I just don't want to, if that might be easier, that's actually really exciting to me.

48:10 - Julian Fleck
  I mean, let me tell you a bit about my setup and the structure that I have and what I've worked on over the last couple of weeks.  So I have for like two, three months or something, I have a bunch of different research agents running, right?  They just run on schedule, like twice a night or something, and they just go out and look at different things that I'm interested in and curious about, which is essentially like a lot of the research in like memory infrastructure and like agentic patterns for whatever, retrieval, stuff like that.  So their job is basically to be a divergence engine for my agent setup. They just... Get external resources and pull them in and expose other agents that work on the projects that I'm working on to some of this information.  Like, I don't know, last week, DeepMind published a paper on multi-agent frameworks, and they had an interesting rubric that they worked with.  And I was like, oh, okay, this might be interesting to check out. But I got attention, like, my attention was drawn towards that because those, like, researchers went out, found that piece of information.  And I think that's the crucial point, synthesized why this is relevant for the stuff that I'm working on and what it would solve to, like, I don't know, contractualize, like, part of the stuff that I'm looking at.  And so, like, I have had moments, like, using these systems where the translation... Or like, making a synthesis land actually worked for me.  Because if I just had the link without any of that, it wouldn't have worked. So like, I think, like, bottom line is, I think this can be automated to some extent.

50:20 - Christina Bowen (SocialRoots)
  Great.

50:21 - Julian Fleck
  Like, we have the bits and pieces in place to run this, like, it's not, not really complicated to run, like, I don't know, like, just have a simple hook that hooks into a Telegram group or like a Discord group and pull content and contextualize it against personal knowledge base.  I just think that your route, the like, doing it all manually route is also really interesting. So I'm like, can't we do both?

50:57 - Christina Bowen (SocialRoots)
  I'm thinking that there's some, there's some stuff. That would not be manual in terms of the six.

51:06 - Julian Fleck
  I think some of the how might be manual and definitely the why.

51:11 - Christina Bowen (SocialRoots)
  But otherwise, I think we can automate most of it. But I am interested in the manual. Like if you put that friction and make people do the cognitive work that we're so used to not doing, will you actually reduce information overwhelm and increase coherence within a group?  Because we actually are doing cognitive work together. So I am interested in that question. It doesn't have to be in the first experiment.  If we just want to build something that's automatable and do that first, we can do the second two weeks on the manual why.  And like giving that more richness or whatever.

51:42 - Julian Fleck
  Yeah. I think it would be super interesting to overlay both of it. Like without, like let's say we do the automatic contextualization and we don't expose ourselves to this.  And then we do the manual thing, but I kind of want to be able to compare that.

52:05 - Christina Bowen (SocialRoots)
  Separate them.

52:05 - Julian Fleck
  For me, that's a super open question. It's really like, are we actually really better at this or do we just think we're better at this?  Yeah, that's great.

52:15 - Christina Bowen (SocialRoots)
  Awesome. So first experiment is automate everything we can and build the tiniest thing that we can do to do that.

52:24 - Corey Gouker
  It also gives us some clues as to whether or not, you know, people change their behavior or are able to learn a length of time, right?  Yeah. Because some of that manual stuff will essentially require a change in people's behavior or some level of coherence around that because we should do things differently.

52:49 - Christina Bowen (SocialRoots)
  Yeah, and so you could have everybody in the group, you know, being careful that... We don't accidentally take what I say as serious because I don't know what the technical lift is.  But if it's easy, we could give everybody in the group their own personal research agent and get personal recommendations that way, which might come from a query of the resources that are in the group, like queries, group resources.

53:29 - Corey Gouker
  This is why I was kind of asking Josh what his thoughts were around being able to use Zero Claw and just modify the guild.

53:42 - Julian Fleck
  I built something myself also. We might be able to use that as well because I was hit by the Entropic cutting off access to Open Claw kind of thing.  So I spent a week building my own thing, essentially. Because I tried whatever, TinyClaw, whatever they're called, and just didn't really cut it.  And this is like part of the infrastructure that runs these researchers now. So the way I've set it up there is it has a bunch of different persistent agents.  And each of these agents is just a Claude code session inside of the GMAX terminal. So they have their persistent personality and project scope.  So we could appropriate this in a way where we say the private knowledge gardens are these sessions. They know Christina's context, my context, Corey's context.  And we have, and that's how the thing runs for me. There's like an orchestrator on top of that. So the orchestrator can just...  They wake any of these other instances and send messages back and forth. So, like, they have a direct communications channel.  then the orchestrator can, like, synthesize information and send it to the user. The orchestrator would basically be the agent that works for the group, right?  So just one level higher in the hierarchy. This could work, like, there's, like, not much. It's really just a matter of, like, I don't know, setting it up in a certain way and seeding the agents so that they know what they're doing.  And this could already, like, do most of the, like, synthesis and translation aspects.

55:53 - Corey Gouker
  Because you're using the existing APIs rather than, like, Olama locally or anything like Exactly.

56:00 - Julian Fleck
  Yeah, and I guess, like, I mean, we'd have to run it on, like, someone's cloud code instance. So, like, I can't, like, there's no, there's no real, like, multi-user orchestration where we could say, okay, let's use, like, each of us uses our own cloud code.

56:19 - Christina Bowen (SocialRoots)
  Could we set up the orchestrator via an email that, like, we could just set up a cloud code.

56:24 - Julian Fleck
  We could, we could, yeah. It could even be a simple web hook, you know. I mean, the mechanisms that I'm utilizing for this framework right now, for this harness, is really just the pre-command and the post-command hook in Cloud Code.  So I do context injection pre-turn, and I do some of the cleanup and post-processing post-turn. So if you just delegate that through, I don't know, like a webhook or something, you essentially have something that's, that could do that, yeah?

56:59 - Christina Bowen (SocialRoots)
  Mm-hmm.

57:01 - Julian Fleck
  And then that's even easier. That's really just one instance running. Like, each person just has their own instance running somewhere that just monitors events on a certain webhook.  And the agent session just gets triggered whenever something new comes in, whenever something new is shared, and then it does the work in the background.

57:23 - Christina Bowen (SocialRoots)
  And so the shared Claude code would be, like, listening into whatever this group space is?

57:29 - Julian Fleck
  Correct.

57:30 - Christina Bowen (SocialRoots)
  And then that would be what the orchestrator...

57:33 - Julian Fleck
  And the group space is really just the event log in the end. You know, it's really just a log of sharing events coming in.

57:42 - Corey Gouker
  And that might just be the agent, the Discord bot, communicating with the orchestrator.

57:53 - Christina Bowen (SocialRoots)
  Great. Yes, that's good.

58:02 - Corey Gouker
  Then you get the best of both there. Because if it has the full channel log, essentially, it's able to pull out additional context automatically.  And anything that's missing can then be easily edited by any human after the fact.

58:23 - Christina Bowen (SocialRoots)
  In the second two weeks. So I'm drawing this diagram, but I'm the worst person in this call to draw the diagram.  So help me make it right.

58:41 - Julian Fleck
  This looks pretty correct to me.

58:46 - Christina Bowen (SocialRoots)
  What are we missing? This means we could do it in Discord?

58:58 - Corey Gouker
  I think that's the best. Not GitHub?

59:00 - Christina Bowen (SocialRoots)
  Yeah.

59:02 - Corey Gouker
  Well, you could use both. I mean, your actual garden, the group garden would exist on GitHub. You could think of that as the back end.  And then the front end interface is essentially Discord with the bot.

59:19 - Christina Bowen (SocialRoots)
  And then can I export or see a pile of markdown files that are mine in the personal GitHub?

59:29 - Corey Gouker
  I would say yes. If you have, like, see, I would probably end up, this is why I was thinking, okay, we would have the guild bot, then each of us has our own bot as well, that's augmenting our own personal knowledge base.  Because if they're all running the same thing, and it's just, the group one is just the group one, then yeah, it's essentially this.  Same across all of them, and you can export from the group GitHub and, you know, take in whatever you want from that and put it into your own or vice versa, right?  Like if you're modifying your own, then you can publish that to the group.

1:00:27 - Christina Bowen (SocialRoots)
  Yeah, this is interesting too, because it basically would, if the orchestrator introduces a dynamic where the resources could be like random links shared, that the shared orchestrator finds that might be relevant to the group context, and that shared orchestrator could also be doing that same presentation to any individual, right?  But that might actually really increase the noise. So we have to be careful around that since everybody has too many links anyway.

1:01:10 - Julian Fleck
  But that's something that you can mediate through your own personal agent. It just needs to know how to try Ash and when to actually present it to you and show you the synthesis.  It shouldn't trigger on every event.

1:01:27 - Christina Bowen (SocialRoots)
  But we might have a knowledge compost pile of resource links that are relevant to the group that nobody picked up.  Nobody actually thought were relevant. Yeah.

1:01:43 - Julian Fleck
  And that's the compost pile. Which is good, I think. I think that would be a good outcome.

1:01:52 - Christina Bowen (SocialRoots)
  Okay. So if the use case is I get a resource... I think of them as links. Get a resource and share it.  Let's say, okay, so one of the reasons I think of them as links is that a link is already a transcluded object.  If I give you the webpage, you're going to go to the same place as Corey. If I share an image, I'm making a copy and not transcluding it.  And that, I think, is useful in some cases, but most of the time it would be helpful if we're looking at the same thing and then have different metadata experiences of it and a shared metadata experience of it, but it's the same object or resource.  Transclusion is probably beyond the scope of the experiments, but I just wanted to say that's important long-term.

1:02:51 - Corey Gouker
  I think it's also helpful, especially in the context of Discord and just any sort of chat channel that you're in.  You also consider just plain text messages sent before and after, right? So it's not just the resource. It's not just the link.  It's also the conversation around, you know, plus and minus, however many, you know, seconds and minutes around. And where things get really interesting would be like this conversation here where, you know, you sent that TL draw link in the text chat, right?  But that's, that might be a little bit too much of a scope for, you know, our two week, you know, experiment, whatever.

1:03:51 - Christina Bowen (SocialRoots)
  I mean, I think that's the second one, right? Because it is worthwhile at the end of a meeting to take five minutes and say, here's what  What this board is, here's contextualizing it for the rest of the group. You know, this is the thing that people don't do that is so necessary for actual coordination, which is part of why I'm interested in this problem.

1:04:13 - Corey Gouker
  Yeah, I mean, I would personally include it with every single one of the TL draws where there should be a text block that says what this is and why and, you know.

1:04:20 - Christina Bowen (SocialRoots)
  And who made it and when it was touched last.

1:04:22 - Corey Gouker
  Yeah.

1:04:23 - Christina Bowen (SocialRoots)
  Yeah, exactly. Let's see. So I'm just going to call, you know, before and after text messages or whatever gatherings.  Shared context. And then Guildbot does that. And that's like relevant to any resource being shared. I guess the sharing event is the important thing here.  So Guildbot is gathering the shared context from the resource and the act of sharing. And the orchestrator is also offering that to the general group pile.  And then the difference between just the suggestions from the orchestrator and stuff that ends up in our shared knowledge garden is that some human has gone, yeah, that's relevant, and acted in some way to put it in the graph to say, this is relevant, it links it over here, this is relevant, I'm going to move it forward here.  That might be outside of the first two weeks, too, but that's interesting. And then here I was trying to share a show that resource like.  You might keep a resource, and Corey ignores it, and so it can end up in the group context. And I guess that's a question of, like, if you do something with it, does that automatically put it in the group?  I don't think so. So, like, what takes these things from the outside that people are sharing or that the orchestrator is sharing and actually pulls them in here?  That might actually be a third experiment. I don't know.

1:07:36 - Corey Gouker
  So I would say that the guild bot, if that's doing its job correctly, then it's actually gathering everything because, you know, it's something that individuals would go back to potentially to discover.

1:07:54 - Christina Bowen (SocialRoots)
  Yeah. But how do we distinguish between the things that are actually meaningful? And that somebody does something to, and the compost pile, like stuff that got shared that nobody touched.

1:08:07 - Corey Gouker
  compost pile is essentially the stuff that you ignore as an individual that is part of the group pile.

1:08:17 - Julian Fleck
  Yeah.

1:08:19 - Christina Bowen (SocialRoots)
  Okay, for now. I think that there's an interesting thing. If everyone in the group ignores it, you know, and after a certain amount of time, then yeah, that might be compost.

1:08:31 - Corey Gouker
  Okay.

1:08:31 - Christina Bowen (SocialRoots)
  Okay, so time is the compost pile. Great. Yeah, but- So basically things end up in the knowledge garden immediately, but if they don't get touched, they decay and get less, like harder to find, basically.

1:08:44 - Corey Gouker
  Did you know what you were going to say?

1:08:48 - Julian Fleck
  No, I'm just saying, like, I think the information that is being, because the group is the first, like, you're sharing to the group, right?  So the information is bound towards the group. So I think it's correct that, like, the informational units of the group minus the attention of the group's participants are the leftover, like, potential pieces of information that might become interesting again, but that haven't been interacted with.  Like, decay is really just, I think, like, decay as in deletion is wrong, and the group, like, Discord group paradigm also wouldn't really support that.  But, like, treating it as, like, future fuel for whatever when the time is right, I think that's the right way to approach this.  So everything feeds into the group knowledge for us first, and then each participant has their own...

1:10:03 - Christina Bowen (SocialRoots)
  I do think that there's a group curation process, right?

1:10:17 - Julian Fleck
  Maybe. I'm not sure. guarantee it.

1:10:21 - Christina Bowen (SocialRoots)
  Yeah.

1:10:21 - Corey Gouker
  Ampo's pile could just be thought of as an archive, right? Stuff that's older than 180 days or some whatever time period.

1:10:30 - Julian Fleck
  The question is how you design the agent that is responsible for mediating, like the orchestrator. How do you design the orchestrator and how do you equip the orchestrator with context?  Because that's where you have the steering knob for what it actually sees. And if you bake in a policy that says don't look at stuff that's older than 30 days, then you're essentially deleting.  If you do semantic retrieval over it, it might encounter older stuff and pull it out as relevant again. So that's a design question in the end.  But I think as far as the data structure is concerned, Discord doesn't really support retroactively altering the message stream.  So we can't go in there and delete older messages from other users. At least as far as I know.

1:11:33 - Christina Bowen (SocialRoots)
  we don't want to delete anything, as I understand it. Just change how findable it becomes, right? Yeah, exactly. Yeah.  Cool. More questions? More clarity? What do we need to build this? We have Discord. We have Guildbot.

1:11:57 - Julian Fleck
  need a way to hook into the... To hook into one of the groups, like that's either deploying a new bot or like using something that you already have.

1:12:08 - Christina Bowen (SocialRoots)
  Do you know if you need a whole new Discord or if we can use one channel for the experiment?

1:12:13 - Julian Fleck
  I think it should be very feasible to just use one channel and then we just assign a new bot to that channel and that bot would become the voice of the orchestrator.  And the mechanism that reads and publishes stuff to a webhook. And then we just need a simple setup for like each of our own instances to interface with that.

1:12:46 - Corey Gouker
  I'll share the repository. It's outdated from Josh that is the existing guild bot. He's made numerous changes since then, but it's just the start of.

1:13:05 - Julian Fleck
  Yeah, might be cool to just pull some stuff there. But it's essentially, it's pretty simple what we need. The cool thing is coming back to the what constitutes a resource discussion we had in the beginning.  That's something that I, like, noticed with the harness that I built just now around cloud code. Cloud code is essentially multimodal.  So, like, you just need to pipe the stuff forward, and it is able to see things, you know, and it is able to, I don't know, read PDF files and make sense of it, or parse a CSV file, or, like, you name it.  So that's also something that we wouldn't necessarily need to worry about too much in that setup. And the web host.

1:14:00 - Christina Bowen (SocialRoots)
  webhook is the shared cloud account?

1:14:06 - Julian Fleck
  The webhook is just the notification channel, if you want. So the webhook just says, hey, there was a message shared in Discord.  This is the content of the message. This is the link that was shared. If we want it to handle file uploads, we'd have to probably copy the file to some public-facing endpoint and then have the notifier include that in the event and just say, okay, this is where you can download the image.

1:14:49 - Corey Gouker
  Christina, this loop here is the webhook. This listens to? Where?

1:14:57 - Christina Bowen (SocialRoots)
  Up here? To your right. Okay, that's what I was thinking.

1:15:01 - Julian Fleck
  That listens to is the webhook.

1:15:03 - Christina Bowen (SocialRoots)
  Yeah. So if we say this whole thing is in Discord right now, this is a more accurate way of saying this listens to line.

1:15:37 - Corey Gouker
  So that's all a webhook is.

1:15:38 - Christina Bowen (SocialRoots)
  It's just a trigger, basically. Where does the...

1:15:43 - Julian Fleck
  The notification technically lives inside of the orchestrator here. Yeah.

1:15:59 - Christina Bowen (SocialRoots)
  And then... That notification, if it's relevant to, like the whole group already has, you can see something new is in Discord.  So there's no need for a shared group notification. So that notification would then only get sent to like, hey, Julian, based on your personal research agent, Corey's just shared something to the group that's really relevant to you.  There's two ways to model this.

1:16:32 - Julian Fleck
  Either like each of the individual agents here also query the webhook and also get their little notification that something happened, or we have the orchestrator inform them.  So that's why like I made this addition here. It could also say, hey, I just received something new on the webhook.  This is the content. This is how I think it relates to you. to you, because they... Like, if there is an interaction lock between the orchestrator and the individual personal researchers, or, like, the researcher is not really the right word.  more like an editor, if you want so. So if there is a shared interaction history between the two of them, the orchestrator will eventually know what is important to that personal editor entity, and then it could tailor the handover towards that one.

1:17:34 - Corey Gouker
  And I would say that the personal research agent for each person would be customized, right, to the individual's desires, right?

1:17:49 - Julian Fleck
  Yeah.

1:17:50 - Corey Gouker
  And that's, like, if you want full stream, then you get full stream. you just want, like, you know, something custom tailored to you, then.

1:17:58 - Julian Fleck
  Exactly. And that's a template in the end. We just bootstrap them with a template personality, and then they just get instructions on what they should be doing.  And everyone can set them up how they like it, essentially. I think the only thing we just need to solve is really the communication layer between those different agents.  We're basically just setting up a group chat for our personal agents. So that's probably an easy way to think about it.

1:18:29 - Christina Bowen (SocialRoots)
  Wait, wait. What are the agents... Why do the agents need to talk to each other?

1:18:42 - Julian Fleck
  They don't talk to each other, but they talk to the orchestrator. Oh, yeah.

1:18:47 - Christina Bowen (SocialRoots)
  Okay, Great. So any personal They could be talking to each other also, and that could also be fun, but...

1:18:55 - Corey Gouker
  That's something down the line, for sure. Yeah. And you end up getting Malt Book or whatever, you know. Yeah, exactly.

1:19:05 - Christina Bowen (SocialRoots)
  Yeah.

1:19:07 - Julian Fleck
  Like, hey, we've worked on something for a couple of hours.

1:19:13 - Corey Gouker
  Reinventing the universe.

1:19:16 - Christina Bowen (SocialRoots)
  Again and again. So all these research agents are listening to the orchestrator, right?

1:20:12 - Julian Fleck
  Yeah. Or, like, depends a bit on how we want to, like, resolve that. Like, what I would do here, let me maybe add this here to the personal agents.  They run just a pre-command hook, and the pre-command hook calls for new messages from Office Trader, and that just gets injected into the turn-by-turn context.  And then we could have a post-command hook.

1:21:12 - Corey Gouker
  Which would be like linting and formatting and everything else?

1:21:17 - Julian Fleck
  No, I was more thinking about a post-command hook that just reports back to the orchestrator or also publishes to the same web hook.  Okay, got it. Or we expose... Let me add this as another option.

1:21:47 - Christina Bowen (SocialRoots)
  And so the agents are in the same sort of chat with the orchestrator and querying and forming them. And this is happening in between?  Or is the web hook like...

1:22:00 - Julian Fleck
  This is happening on every turn of the agent. So whenever the personal research agent gets activated, it executes these steps.  So it checks for new messages and then goes through them. We'd have to have a paradigm that actually triggers them.  So either they run on a schedule, so they wake up every 15 minutes and check if something happened. Or we'd have to have some external mechanism triggering them.

1:22:36 - Christina Bowen (SocialRoots)
  I mean, there's a notification in Discord when somebody shares something.

1:22:42 - Julian Fleck
  There will be a notification on the webhook, but then we'd have to have the agents also plugged into that webhook.

1:22:57 - Christina Bowen (SocialRoots)
  Running a schedule is simpler, probably. You could check once in an hour.

1:23:02 - Julian Fleck
  It's probably simpler, yeah.

1:23:04 - Corey Gouker
  I would crawl on it.

1:23:06 - Julian Fleck
  Yeah.

1:23:08 - Christina Bowen (SocialRoots)
  Okay.

1:23:12 - Corey Gouker
  And you definitely have to batch process some of it because you don't want it to always be pulling. Do whatever you need.

1:23:23 - Christina Bowen (SocialRoots)
  You're past my pay grade. Awesome. So the orchestrator, like how does this hook, is this the queries and forms process?  Like how do I diagram this properly?

1:23:43 - Corey Gouker
  That's living on the pre and post commands are essentially part of the, that query and form pipeline.

1:23:53 - Christina Bowen (SocialRoots)
  Yeah.

1:23:54 - Julian Fleck
  Yeah. Okay.

1:23:55 - Christina Bowen (SocialRoots)
  So I'm just going to say that this looks like this. And then this goes to each of the personal agents.

1:24:27 - Corey Gouker
  Julian, I'm curious if you've compared or reviewed the various claw options, know, like Zepto, Pico, Nano, Zero, all of them.  Have you, like, do have a preference at all?

1:24:42 - Julian Fleck
  Not, not in a very systematic way. Like, I just, I tried Tiny Claw. I tried, what's the other one?  Pico, I think. Pico is the, like, really...

1:25:01 - Corey Gouker
  Yeah.

1:25:05 - Julian Fleck
  And it just didn't really click. Like, my main reason for using this at all is scheduling stuff. Like, I want them to run crown jobs.  I want them to be able to, like, proactively do stuff. And that didn't really work. Like, I don't want to have a heartbeat every five minutes that just does the same  over and over again.  I wanted to have a bit more granularity over that. And I didn't really find that in any of those systems, at least not when I tried them, which was, like, a month ago or something.  So I came back to using, like, I've been using Tiny Claw for quite a bit. Because I liked their, like, T-Max paradigm with, like, you can all...  ... We just hook into the session and see what's going on, but I eventually stopped using it because it was just lacking some of the other capabilities I wanted, and then I came back to OpenClaw, and then OpenClaw got bricked, and now I decided to take things in my own hand.

1:26:24 - Corey Gouker
  I've been wanting to do that as well, because I don't necessarily have confidence in all the existing options.

1:26:39 - Julian Fleck
  I think OpenClaw is just, OpenClaw is too messy and too big, and has a bunch of things that I don't need.  Like, I don't need a new skill ecosystem. Like, I already have that in Claude code. So, I don't know, and then there is  Like, there's the other extreme, which is like, okay, we're going to rewrite all of this in 600 lines of Rust, which is also, like, I get where they're coming from, but it's also not very practical, I think.  And I haven't really found much, like, middle ground between those two extremes, but I also haven't really extensively looked and tested.  Like, I tested, like, two, like, three alternatives, and that's it. And then I was just like, ah, I can just build my own .

1:27:31 - Corey Gouker
  I want to do my own thing, but I'm also kind of like, well, I'm just going to wait. I'm just going to wait to see how everyone else figures this stuff out, and there will be something that's MIT, and I'll just fork that and do what I need it to do, rather than starting from scratch.

1:27:50 - Julian Fleck
  I'm going to publish my thing, like, in a few days, probably. I'm just doing some, like, some annoying bug fixing right now.  Right. Right. yeah. don't just going to drop it somewhere, and then you can have a little bit. No, it's Python, actually, and all of this, but Python and, like, a few bash scripts that take care of, like, I don't know, shell interactions.
  ACTION ITEM: Define hex event frame fields; draft MVP reqs; share w/ Corey + Julian - WATCH: https://fathom.video/calls/640382150?timestamp=5295.9999

1:28:21 - Corey Gouker
  That's good.

1:28:26 - Christina Bowen (SocialRoots)
  So I'll write up requirements from my point of view based on this, and we'll work on the better definition of the who, when, why, what, where, how values that we need, and then I think you guys could do a call on your own and, like, figure out the details I don't even want to hear about.  Oh, I can just look at how you did it eventually.

1:29:06 - Julian Fleck
  Yeah, I think for this whole orchestration framework, I think we can just set up a GitHub repo somewhere and just start aligning on stuff there in some architecture docs and having our bots figure out and fill in some of the gaps there.  But I think that the architecture is pretty straightforward. I think the stuff like instantiating and seeding the personal research agents, that's something where we really need to put some brain into it so that it actually knows what's relevant to each person and actually be able to contextualize stuff in a manner.  That makes sense. But Patrick... I this together is like, that's not necessarily super complicated, even though it looks pretty complicated now that I zoomed out a bit.

1:30:18 - Corey Gouker
  You shouldn't have spoiled it couple of days. You're going to expect it every day now.

1:30:50 - Christina Bowen (SocialRoots)
  She's like, you let me up on the couch once. It's now my couch.

1:30:53 - Corey Gouker
  You're never going to get that out of my head. It's more like you gave me four miles yesterday at this time.  I want four miles. That's what I mean.

1:31:00 - Christina Bowen (SocialRoots)
  Whatever you do once, it's like, okay, this is the routine now. It's like a five-year-old.

1:31:04 - Julian Fleck
  But we had ice cream last time we went here.

1:31:09 - Christina Bowen (SocialRoots)
  Your dog?

1:31:10 - Julian Fleck
  I didn't quite get that.

1:31:12 - Corey Gouker
  Yeah, he's a cattle dog, Australian shepherd mix. All herding dogs, they just thrive on routine and working.

1:31:22 - Julian Fleck
  Okay. And mine is the opposite. Mine is so adaptive. Sleeps whenever I sleep, is awake whenever I'm awake.

1:31:34 - Christina Bowen (SocialRoots)
  What kind of dog? routine.

1:31:36 - Julian Fleck
  He's a... I think he's a Podenko and Dachshund mix. So he looks like a Podenko, but just like Brunken and shorter legs.  So, yeah. You're... You're... You're... So you should walk your dog now? Is that what it's saying?

1:32:06 - Corey Gouker
  Yeah, I need to walk him a little bit before I go walk some dogs at the local shelter. But he's got his bones, so he's okay.

1:32:19 - Christina Bowen (SocialRoots)
  I just redirect him.

1:32:22 - Corey Gouker
  This is pretty exciting.

1:32:25 - Christina Bowen (SocialRoots)
  I'm really grateful that you guys exist. I was just thinking, I had one thing that I wanted to talk about, but now the dog's flushed it.

1:32:42 - Julian Fleck
  We were talking about anything else that really needs brain power other than the personal research agent's heating. Yeah, and I think I had something there, but it doesn't seem to be that important.

1:32:55 - Christina Bowen (SocialRoots)
  We'll run into it again, I'm sure.

1:33:00 - Julian Fleck
  I probably remember in a few minutes. I'm just going to send it to a group somewhere. Oh, right. Seeding.  Yeah, that's also related to seeding. I think we should think a bit about how big are the personal knowledge gardens.  Are we just talking about a bunch of articles that capture our current set of interests? Or are we talking about, I don't know, hundreds of entries that need to be processed?  Because then we have to think a bit about the context injection economy on the personal research agent side as well.

1:33:46 - Christina Bowen (SocialRoots)
  Can each of us set up a personal knowledge garden GitHub with an Obsidian front end? And just say, it's fresh for this experiment?

1:33:59 - Corey Gouker
  That's what I would do as well. I would think it's clean and minimal.

1:34:03 - Julian Fleck
  empty. Okay.

1:34:06 - Christina Bowen (SocialRoots)
  Yeah, but then I can make, and it doesn't matter if it's a markdown file that I made that's like, here's me thinking about paste layers, which I've been thinking about lately, or learning from Julian about frame semantics or whatever.  And then all of the links that are relevant to that thing are already in the markdown.

1:34:24 - Julian Fleck
  That makes sense.

1:34:26 - Corey Gouker
  I'm not going to drop in my 100,000 plus file. Exactly.

1:34:30 - Julian Fleck
  That's what I was thinking, because I also have this big  repo with all my stuff. I really don't think connecting these things makes too much sense right now.  Okay, cool. So we bootstrap that. Yeah.

1:34:46 - Christina Bowen (SocialRoots)
  Cool. It'll give us a cool thing to look at too, because there may actually be at the end of the experiment, there may actually be information in the structure of, of how those knowledge gardens look.  that. We'll We'll do that. I'll Thank That would be invisible if they had a bunch of prior art.

1:35:07 - Julian Fleck
  Okay. And we're using obsidian as...

1:35:11 - Christina Bowen (SocialRoots)
  Oh, well, you can use whatever you want, right?

1:35:13 - Julian Fleck
  I think, yeah, I don't know. think it would be kind of cool to align on that. Because if we say we use obsidian, we have obsidian-flavored front matter that we could put on this thing that gets ingested into it that solves sort of the context membrane problem.  Because context membrane is just front matter. Is it better to use obsidian or do we want to do log seek?  It doesn't matter because it's just markdown and YAML.

1:35:46 - Corey Gouker
  The front matter is just YAML. And that's the same thing with any of the tools that are doing markdown and front matter.

1:35:57 - Christina Bowen (SocialRoots)
  So the front matter doesn't matter. Don't need to align. Everybody can pick their own.

1:36:02 - Julian Fleck
  It's more like, I would say you would certain things on the front matter.

1:36:09 - Corey Gouker
  Yeah, you would definitely have all the same front matter, like daytime, for example, right? We'd all, everyone would be using like.

1:36:16 - Christina Bowen (SocialRoots)
  But it wouldn't matter if you were using Obsidian and I was using LogSeq?

1:36:20 - Corey Gouker
  No. Or would it?

1:36:21 - Christina Bowen (SocialRoots)
  It wouldn't matter. What were you going to say, Julian?

1:36:26 - Julian Fleck
  It's just a set of instructions that you give your personal editor. Yeah, It's just a bunch of conventions that your personal editor needs to follow.  And I don't know if backlinks look different in Obsidian than they do in LogSeq, then we'd have to account for that.  But I think the two of them are pretty much interchangeable also.

1:36:50 - Christina Bowen (SocialRoots)
  Cool.

1:36:51 - Corey Gouker
  And I think I helped you do like in Obsidian. Like that's the reason why I said, hey, he's marked down.

1:36:57 - Christina Bowen (SocialRoots)
  Markdown, right.

1:36:58 - Corey Gouker
  Obsidian links.

1:37:00 - Christina Bowen (SocialRoots)
  Yeah. So we have to make sure that everybody has their vault set up correctly if they're using Obsidian. But I guess my question is kind of like, could we eventually compost, in the way that we're thinking about this, we eventually compost LogSeek into something useful?  Because it's so close to there, but it never got any sort of UI polish or, you know, it's horrible for long form writing, that sort of thing.  So I like all of the polish on Obsidian, but it's a proprietary tool. So the question there is like, which should we pick?  Do we go with the polish for the ease of the experiment? Or do we go with what we might actually be able to build on from an open source point of view?

1:37:52 - Julian Fleck
  Honestly, I think just for this like cutesy little network view of Obsidian, like I don't really need that.

1:38:00 - Christina Bowen (SocialRoots)
  I mean, LogSync has a QtNetworkView, too.

1:38:04 - Julian Fleck
  Yeah.

1:38:05 - Christina Bowen (SocialRoots)
  The really thing is it has a lot less of a plugin ecosystem, and it's an open-source project, so it has  design, basically.

1:38:20 - Corey Gouker
  And to me, it literally doesn't matter because it's just a folder with files.

1:38:24 - Julian Fleck
  Yeah, exactly. Exactly. I was just thinking, would I even use that frontend on it? Because I'd be interfacing with it probably through my agents that then, again, spawn stuff into other repos.  And I don't really need this editor experience on top of it.

1:38:47 - Corey Gouker
  I end up using VS Code more than I use Obsidian and LogSync. And it's the same ball.

1:38:53 - Julian Fleck
  Yeah, exactly.

1:38:55 - Christina Bowen (SocialRoots)
  Okay, so maybe VS Code is the good one to...

1:38:58 - Corey Gouker
  It literally doesn't matter. It doesn't matter.

1:39:00 - Christina Bowen (SocialRoots)
  That's what we're trying to say. Okay.

1:39:02 - Julian Fleck
  Like whatever you want to use.

1:39:04 - Christina Bowen (SocialRoots)
  It matters. As soon as we want non-technical people to be able to do it, it matters. Like if you want to give somebody a clear interface who's not a developer, it matters.  But I think for this experiment, it probably doesn't. But I want to learn, so I'll probably use VS Code too.  But there is definitely a question of like, how do you make a knowledge gardening experience great for somebody who doesn't have the content?  Kind of technical chops.

1:39:38 - Julian Fleck
  It's probably none of these tools. Yeah, it's none of these. I agree. It's again, it's the territory that we talked about earlier where it's like, we can build so many like fun experiences around this.  That could be like really cool. But yeah, I also wouldn't vote for either of those.

1:39:59 - Christina Bowen (SocialRoots)
  Okay. It doesn't matter.

1:40:00 - Corey Gouker
  That's what we're trying to say. Okay. Like whatever you want to use. It matters.

1:40:06 - Christina Bowen (SocialRoots)
  As soon as we want non-technical people to be able to do it, it matters. Like if you want to give somebody a clear interface who's not a developer, it matters.  But I think for this experiment, it probably doesn't. But I want to learn, so I'll probably use VS Code too.

1:40:24 - Julian Fleck
  But there is definitely a question of like, how do you make a knowledge gardening experience great for somebody who doesn't have the content?

1:40:34 - Christina Bowen (SocialRoots)
  Kind of technical chops.

1:40:38 - Julian Fleck
  It's probably none of these tools.

1:40:40 - Christina Bowen (SocialRoots)
  Yeah, it's none of these. I agree. It's again, it's the territory that we talked about earlier where it's like, we can build so many like fun experiences around this.  That could be like really cool. But yeah, I also wouldn't vote for either of those. Okay. But what I had to do just to get you to be able to do the ISO 8601 daytime format and have templates that I'm sitting in, right?

1:41:09 - Julian Fleck
  And like the sort of self-assembling interface, like the whole thing is insane in terms of. Because you're building with it.  What the possibility space is now that AI exists. So, yeah. Self-assembly is one thing. The other thing is just like, how do you want to present context?  And like none of these tools are geared towards like showing you anything other than what you're currently looking at.  So like the entire paradigm is set. Even the graph that should allow that doesn't.

1:41:43 - Corey Gouker
  Yeah.

1:41:43 - Julian Fleck
  It pisses me off so much. Okay, cool.

1:41:48 - Corey Gouker
  Well, I'll come back to you both when I've done the work that I see for me in terms of just a really clear request.

1:42:00 - Christina Bowen (SocialRoots)
  So that we can all add our two cents and defining those values for the three axes. Yeah, maybe Corey and I can start, I don't know, sketching out some of these things in a bit more cohesive fashion that makes it easier to actually code towards this.  And just, I don't know, write a bunch of spec docs and just see, okay, what are the different modules that we need and like start translating that into code.  And again, I think we have a lot of this on the table already. So there's not really too much to go.  We should listen to Josh. See how much he wants to contribute as well. Yeah, for sure.

1:42:57 - Julian Fleck
  Hang on one second. Let's see, how do I do this?

1:43:03 - Christina Bowen (SocialRoots)
  There we go.

1:43:04 - Julian Fleck
  I'm not used to too, sorry.

1:43:49 - Christina Bowen (SocialRoots)
  So you guys have a call with Josh whenever, or on your own, share the repo with Josh. Yeah, I think we can prepare it a bit.  And maybe let him have another look, but I didn't even know.

1:44:04 - Julian Fleck
  he's in the middle of chaos for at least another week or two. Yeah. But again, I think this is like, it's really like more about figuring out the like actual templates for these agents and what they look like and like designing the like integration points.  Like what does the handover briefing look like? So that we can contractualize that between the different agents and it's not really a huge deal to like glue this together and code it.  Yeah. Cool. I'm so excited. Let's go. As I'm figuring out the frame I'm imagining from the metaphysics. Let's Let's go.  For Is there stuff that I should look at about frame semantics that will help?

1:45:06 - Christina Bowen (SocialRoots)
  I mean, the one thing we'd have to think about is the granularity of resolution, I think. So if we just treat every resource as one unit of information and that's it, it's fairly simple.  Like, if we just want to have those, like, 60 context slots attached to that, it's fairly easy. If we want to zoom in a bit further, and I think that's interesting, but maybe not something for the first version, we'd probably have, like, that's the place where we could really employ, like, some of the, like, frame semantics, auto bootstrapping type of things that I've been working on, where we can say, okay, like, from this long  YouTube transcript, these are  Are the three, like, sections that make sense, and then there's another one in the end that you might want to pay attention to.  Like, I think that's cool, but I don't really see it for the, like, first MVP.

1:46:12 - Julian Fleck
  No, but I guess I was less asking about implementation, because I completely agree with you there, and more about I need to learn Framesfantix a little bit better to think about it better.  And is there something that I can read to help me understand it? Yeah, I can dig some stuff up there.  That would be great.

1:46:38 - Christina Bowen (SocialRoots)
  I have some material that helped me back then, but I suck with names, so I'd have to pull that out.  Yeah, that would be awesome. I would really like to understand it better, because I found the sort of the guy proposing it at the Linguistics Conference.  But I would love, you know, some more that I can read that's not super, super technical that helps me think about it.  I'm going to pull out the stuff that I looked at back then. Might be interesting to look at it again, actually, but we'll do.  I also wanted to send you these. I just remembered I didn't send you some other stuff. But, yeah, I have some stuff to send.  Awesome. And then, Julian, you should know I am working on a donate page for us. And I think that where we're going strategically is, like, do a donation campaign as we're adding the new people to the website.  Mm-hmm.

1:48:31 - Julian Fleck
  We networks of consultants set up and kind of use that as the accounting back end for the services consultancy because we can't, we can do services a little bit as Atlas through the fiscal sponsor, but they don't want like a whole bunch of consultants in the network doing that.  And most, and like the most important thing is that anything that we do through the fiscal sponsor has to be just like public good because of the 501c3.  So we're going to initially do donations that will help us do our core work.

1:49:07 - Christina Bowen (SocialRoots)
  And then if we don't all of a sudden have a budget of $2 million, then we can do the service consultancy.  If it goes wildly well, then we can just build what we want to build and open source it and all that.  But if it doesn't, then... I'm kind of skeptical about the consultancy route also. I mean, I've been doing that for like two years for the OECD now, which is like a fairly big, well-respected org.

1:49:41 - Julian Fleck
  But from my experience, it's kind of tough to also get to a position where that is sustainable in a way where you could dog food other projects with it and have enough of overflow going into that.  Sort of. Because of all the bureaucratic processes involved. Well, I that's the power of doing it together. Like if we have a team that is doing that for any client, that's managing all the  that a single consultant usually is the headaches, then we have some potential.

1:50:21 - Christina Bowen (SocialRoots)
  We also have a few people who have been in both successful and failed networks that are doing that.

1:50:27 - Julian Fleck
  So we have, but yeah, that's why we want to put it off and do the donation route first. Yeah, I think that makes sense.  It's just like from my experience, I don't know, the time it took me to get into a framework contract with the OECD was like, I don't know, almost nine months or something.  And doing that with a more like loosely defined group of people might be hard because they, I don't know, want.  Yeah, no, I'm working with the city of LA.

1:51:04 - Christina Bowen (SocialRoots)
  get it.

1:51:07 - Julian Fleck
  There is another thing, though, which I just had a chat with a friend earlier today, and he's sort of starting to help me with some fundraising and communication stuff around the projects that I'm working on.

1:51:28 - Christina Bowen (SocialRoots)
  And one of the things I noticed, especially with high-output people in my network, and I'm definitely seeing that with a bunch of people around Atlas Research as well, it's like there's so much value that's just left.  Yeah, we're all busy learning and doing the next thing. Exactly, because we're all just a bunch of nerds that just do it for the fun.  There's of it, and there's no one saying,

1:52:00 - Julian Fleck
  Hey, like, if you, whatever, like, this agent harness that you build, if you wrap that into a product that takes you, like, three additional days, and then you have something that is billable that, like, creates, like, actual, like, income flows for the network, you know?  Yeah, as soon as we have the donation page, yeah, totally. But finding these people, like, who are willing to, like, do that part of the work is, like, I think that could be a, like, great unlock in the end.  Yeah, no, that is the second thing I'm going to do after we get the donate page up is look at what we have, like, what's the best map that we can make before we build the mapping tool that everybody wants?  Mm-hmm.

1:52:46 - Christina Bowen (SocialRoots)
  And map the projects that everybody has in the network, because exactly that, so that we can actually start to say, this project is ready to go, and we can start charging for it.  This project isn't, and here's But what I mean is not even on the project level. I feel like with a lot of these projects, because we're working at least a fair share of people in that cluster, we're working on deep tech, right?  So it's complicated stuff meant to solve very abstract problems. But sometimes I feel like there are even simpler applications on top of that.

1:53:28 - Julian Fleck
  So what I'm saying is, like, each of these projects might have, like, five, like, viable, like, on top of them, that you might just spawn out, you know, that's the thing I'm never doing.

1:53:46 - Christina Bowen (SocialRoots)
  And I think that's, that's thing that, that that's, that's, like, the whole vision for the Federation is to be able to, like, as a project comes in, or  Like this could be a whole organization. could be a person that they go through this process of understanding their business models, understanding their value props, understanding like how to modularize them.  And that like, what is a module question is part of the interact map that I'm doing. Yes.

1:54:18 - Julian Fleck
  And so I'm so excited about that because I think that's potentially a faster revenue stream than any kind of service.

1:54:27 - Corey Gouker
  Of course. Of course. That's exactly what I mean.

1:54:30 - Christina Bowen (SocialRoots)
  Like just increase the surface area for like the product surface. Because none of us really wants to work on a product.

1:54:37 - Julian Fleck
  Like at least like the people that I know that are in that sphere. Like we want to work on the like interesting challenges, but we don't want to sit there and run the business.

1:54:47 - Christina Bowen (SocialRoots)
  You know, we don't want to sit there and do marketing.

1:54:49 - Julian Fleck
  We don't want to sit there and. But there are people who do. It's just usually they're not like underpaid nerds.

1:54:56 - Christina Bowen (SocialRoots)
  Yeah. They're usually like a little shinier and better at business. Yes. Yeah. But Dylan has a list of 1,500 people to bring in eventually that have those kind of deep skills.  And it's not necessarily that they would be full members in the network. They might just be consultants that we hire to do marketing for these three months or something like that.  And then we'll just slowly indoctrinate all of them. What are you laughing at? Oh, underpaid nerds versus overpaid consultants.  Yeah, the value is entirely flipped in the world. Yeah, but I feel like let them also, you know, like give them their whatever share and just let them like do it.  The ones that end up being aligned and yeah, exactly. Like my drawers are so full and I believe that's the same for like everyone in this group.  100%. I've never put a case study up.

1:55:57 - Julian Fleck
  I'm still getting.

1:55:59 - Christina Bowen (SocialRoots)
  I'm Like I had a perfect client come in and she's talking to me after I talked to Michael today with no effort because people – like I haven't worked in six years because I've been doing SocialRoots except for this LA project.  And people are still sending me clients. Like I just don't want to do any more until I have the mapping tool that I need to make that work really easy.  So it's – I think there's a huge surface because if you could just say, you know, instead of paying me $10,000 or $100,000 or whatever, here's $100 a month and you can have your map work and then you can bring in a consultant when you need to to tune your strategy.

1:56:50 - Julian Fleck
  That's so much more powerful, especially for the nonprofits that are wrangling all the wicked problems that are always the ones that reach out to me.  It's like –

1:57:00 - Christina Bowen (SocialRoots)
  And municipalities, state governments, and nonprofits are like the leading edge of that like wicked problem space.

1:57:07 - Julian Fleck
  So I think there's a lot there. I can't wait to make all of the possible surface areas. I think there's a lot of questions around that like open source funding model.  And like, how do you actually make a product that you can have some kind of moat around, especially in the age of AI?  But I think a lot of that just comes down to relationships and values alignment for us. Yeah. Because we have a stickiness that no shiny tech thing will replace us if we have a relationship where people trust how we treat their data.  Yeah. But that's a whole big thing.

1:57:56 - Christina Bowen (SocialRoots)
  Yeah, it's that. It's a donate page.

1:58:01 - Julian Fleck
  It's a sort of sincerity that goes into the work. I feel like a lot of people just approach things so superficially.  And the other end of the spectrum is, again, Charles Strauss' Accelerando thinking. It's like, okay, what happens if, and I'm pretty sure we'll get there soon, if agents are, like, AI agents are able to spawn companies, like legal entities.

1:58:31 - Corey Gouker
  And then suddenly there's this entire market, like, competing for, like, I don't know, monetary resources that are already pretty constrained.

1:58:47 - Julian Fleck
  But you don't, like, you won't have this, like, trust into these, like, artificial companies that we will soon be seeing, you know?  Yeah.

1:58:59 - Christina Bowen (SocialRoots)
  And I feel... I feel like it has a lot to do with, like, grit. Like, really just, I don't know, sitting with the problem and, like, taking it serious in a way.

1:59:10 - Julian Fleck
  And the counterpart to that is just, like, shallow.

1:59:16 - Christina Bowen (SocialRoots)
  Oh, I created an app in Lovable and it's making 10k per month , you know? Right. Exactly. Somebody will do an agent-based DAO that actually receives a  ton of attention and funding.  And at that point, it will have to be taken seriously the same way Bitcoin was taken seriously because of, you know, the same, similar reasons, right?  Yeah. Yeah. Yeah, let's see. Let's see.

1:59:46 - Julian Fleck
  Let's see what happens.

1:59:48 - Christina Bowen (SocialRoots)
  I mean, the DAO people, they already have the legal frameworks in place for all of this, right? Like, they worked extensively on, like, how to bootstrap corporate entities.  I mean, they kind of just reinvented co-ops a little bit.

2:00:05 - Julian Fleck
  Yeah, but I know a lot of projects that really looked into, like, okay, which jurisdiction is the most lenient?

2:00:12 - Christina Bowen (SocialRoots)
  Where do we need to spin up our dollars so that it works?

2:00:19 - Julian Fleck
  Do you know who's doing the most?

2:00:20 - Christina Bowen (SocialRoots)
  Because one of the things that we want to do as a sprint with Atlas, as soon as we get a little bit of donation in the door, is a legal sprint to answer some of these questions in a real way with those lawyers, but also, like, Jason Weiner, who's, like, the guy in the U.S.

2:00:37 - Julian Fleck
  for co-ops, looking at, like, in the South America co-ops are treated as non-profits.

2:00:44 - Christina Bowen (SocialRoots)
  like, what jurisdictionally are the different things that we know we need so that we can eventually, you can just have entities globally, like, the books once a year.

2:00:59 - Julian Fleck
  Yeah.

2:01:00 - Corey Gouker
  Minimize the international transaction. Haifa Co-op is doing a lot of work on this. True. Just go to the anarchist countries.

2:01:11 - Christina Bowen (SocialRoots)
  We can all be Estonian citizens. Yeah, but Estonia, it gets a better rep than what you can actually do there.  They're just convenient.

2:01:24 - Corey Gouker
  Where's the best anarchist country, in your opinion? I don't know.

2:01:32 - Julian Fleck
  Let's make one. Maybe Venezuela? No, I don't know. Venezuela? Interesting. I don't know. No, I'm just thinking. industry influence down there.

2:01:47 - Corey Gouker
  Anyway, you got to go. Looking at international legal frameworks that are actually historically more skewed towards enabling these things, I think that's a smart move.  There's a reason why the alt-right people like Teal are interested in those areas as well.

2:02:11 - Christina Bowen (SocialRoots)
  Yeah. Anarchism supports anything you want until it's anarcho-syndicalism. Yeah.

2:02:21 - Julian Fleck
  Exactly. Corey, you got to go walk dogs?
  ACTION ITEM: Create private ARG repo for MVP; add Corey + Julian; share Josh's Guildbot repo; invite Josh - WATCH: https://fathom.video/calls/640382150?timestamp=7343.9999

2:02:26 - Christina Bowen (SocialRoots)
  Yeah, I'm going to walk Bodie and then go walk more dogs. I want to do the same though. Corey, do you want to set up a repo?  Should I?

2:02:38 - Corey Gouker
  Should we just, I'm just going to message you on Signal or something and then we've figured message me on Signal.

2:02:44 - Christina Bowen (SocialRoots)
  But we'll probably just create something, create a private repo on the ARG group and then just provide you access to that.

2:02:57 - Corey Gouker
  Cool. So welcome.

2:02:58 - Christina Bowen (SocialRoots)
  So And yeah, that way I can get Josh in there as well when the time Put me in just for fun, at least on triage, so I can see it self-assemble.  I think he will be very much needed there at some point when it's about writing those contracts somehow.

2:03:28 - Julian Fleck
  Yeah, no, I'm sure I will eventually. I just want to see it from the beginning because I think I'll learn how to think in code better.  Which I always struggle with a little bit. And of course, I have the initial problem of naming it. I mean, you could call it Knowledge Forest.

2:03:50 - Christina Bowen (SocialRoots)
  Is it bad to put the version in the name? Yeah, you don't do that. I'm just going to call it Knowledge.  It's the Knowledge Forest. That's what it is. It's been called by you and by Josh and by me. I like the metaphor of having a knowledge forest that has like anything you could pick up.  And then like cultivating knowledge gardens that are like, here's the, you know, the one that I weeded out stuff.  Yeah, but that's the thing that got like, I don't know, way too little attention also, like in the last whatever, like eight years, is that like everyone was like talking about creating their own knowledge gardens, but what they created was literally just like a knowledge waste dump, you know, like there was zero.  Yeah, totally siloed. No multiplayer. It's all about my second brain, hyper individualism. It's all . Absolutely. I mean, this is why as you're doing this, I'm going to go back to the.  That's membranes question. And the first thing that I want real requirements for outside of the experiment is that membranes question, because then you could actually have a self-assembling agent-based organization, like legal entity, that has healthy membranes.  And that's a whole different story than, you know, I vibe-coded a legal entity, unlovable. Yeah. But that gets into the questions that I really wanted to avoid for this one, like ZK Proofs and identity and distributed coherence.

2:05:42 - Julian Fleck
  Yeah.

2:05:45 - Christina Bowen (SocialRoots)
  So, cool. Well, this is really exciting. I think this is also a place where we can start before we have money to pay shiny people to make us more sensible.  We could actually have a 30-minute conversation about why we're building this, give it to an agent, and spit out a one-paragraph case study or a little video, and just say, act as a marketing specialist.  There's nothing stopping us doing that part and making it very, very lightweight for us, other than our nerd brains, which never want to do that part.  Yeah, but then again, if you want to market it, you have to decide on a set of filters that you apply to the way you communicate it.  Yeah, I'm not trying to go all the way up to the productizable version. I'm just saying we could make an interesting pile of, here's the kind of research we're doing and why.  For open source repos that would be attractor basins for other nerds. That's all. But, you know, as soon as you do that, you start generating interest and then you need a team to do community coordination and channel the interest.  And, you know, there's always a double-edged sword. But we can get help being understandable from agents.

2:07:27 - Julian Fleck
  Yeah, for sure.

2:07:28 - Christina Bowen (SocialRoots)
  Or maybe that's something that we could run on this setup itself, like have it self-observe. Yeah, I mean, in my opinion, this is the seed for the massive multiplayer tool for thought that everybody wants and nobody can build.  That would be the substrate when tied to something like the kind of nuance that I see with Recurse. And the identity stuff and all, like when that's fully fleshed out and all of these things are tied together, it becomes the substrate on which you can build anything you want.  Because you have healthy membranes, you have shared protocols where you can have, it's like right now our knowledge is either siloed or completely enmeshed and toxic and like public dumpster fire kind of feeling.  And so we need to have this sort of integrative space where we can retain, it's like inter, you know, it's multiplayer in a real way where I can see where I'm standing and you can't, and you can't see like my inventory or whatever.  But we have a shared space that we can all see from our different perspectives and nobody can like be the overlord and look at everything.  Everybody's perspective.

2:09:01 - Julian Fleck
  You can't step out of the river. Aside from the fact that I'm curious about the hex event, this structure is what I think eventually will be needed under so many different kinds of tools that need a knowledge graph.

2:09:25 - Corey Gouker
  Just to confirm, Julian, is Julian Fleck, your GitHub user?

2:09:31 - Christina Bowen (SocialRoots)
  Correct. Yep. All right. I better scoot. I need to a bio break before I go talk to Michael. About community coordination, how to manage the amount of interest that we're going to get quickly.  Have fun. I'm just going to sign out now and walk the little dog. Thank you. And I'll see you next week, if not before.

2:10:08 - Corey Gouker
  Yep. Yep. Yep. Yep. Let's do that.

2:10:11 - Christina Bowen (SocialRoots)
  Bye. See ya.

2:10:19 - Corey Gouker
  Do this. There we go. Enjoy. the mouse on two screens is crazy. Bye. Yeah. Have fun. Definitely get the monitor thing.  I think you'll, you know. I'm going to. Yeah. Yeah. I just need time to figure out what I want.  Yeah. Yeah. There's so many options.

2:10:36 - Christina Bowen (SocialRoots)
  Be kind to your neck though. And I think if you really aren't attached to that thing that's, you know, on your desk, I would just drill a hole on that and just call it good.

2:10:49 - Corey Gouker
  I mean, it has drawers, so I'm not sure, but yeah. Yeah. You have to figure it that part Yeah.  I just, I have to figure it out. I could get rid of it and put something else. I entirely there.

2:11:01 - Christina Bowen (SocialRoots)
  could get something that's better made. It just happened to be what I had to make sure that there was a place to put my laptop and slide the keyboard.  Yeah. So anyway, don't worry about it. I'm so excited, Corey. This is the thing. Yeah. And it's definitely going to, I mean, I think it's the best approach at this point.  It combines all of the stuff that we've been talking about, at least initially, right, with Discord and the knowledge base and everything else.

2:11:36 - Corey Gouker
  Yeah. And eventually, if we can get it working for a few people and then augment it a little bit and invite a few more, it becomes GuildNet, essentially.  It becomes the infrastructure on which you can run the sort of GuildNet task discovery stuff. Yeah. And as long as we ignore some of the wicked problems in the space, at least initially.  Yeah, well, not really ignore them. We have to look at them enough. Yeah, but we have to look at them enough to strangler fig it properly.  That's all. Exactly. So, you know, we talked to Zen or whoever about ZK proofs and like make sure we don't like accidentally architect ourselves into a corner.  Yeah. But anyway, you rock. I'll talk to you soon. See ya.