# Make it work

I've started the test through the backend because I am not as familiar with Python as I am with React, and I prefer to start with the hardest part.

It took me a lot of time to manage to make the application work locally due to very different issues across most of the technologies in the project. This means running and testing the app.

At the mean time, while I waited deletions, installations, and updates, I created a file to track [improvements](./IMPROVEMENTS.md), which I won't tackle at the moment. Even the ones that I think would improve how I present the test because my priority is building the required feature.

Part of making the app work was doing small changes on the current tooling, I hope this is okay. This includes adding [ASDF](https://asdf-vm.com/) [tooling file](./tool-versions).

# S3 Download

As this is the required feature for BE, I am jumping to implementign it.

The idea is to separate a service for object storage, which is different from the current repository because they handle different concerns.

And probably next iteration will have the repository wrapped in a service class, to which the API layer talks to. Such service class would wrapp the repository and the file storage.

For the exploratory testing, I'll cheat a bit and use a different repo I have that reads from s3 buckets to see if the PDF is read successfully. This way I'll this faster during FE development time.
