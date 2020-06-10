## GitHub Actions to post anime GIFs on Slack

Sometimes you want to react to an event on GitHub with a message on Slack but words are not enough.
This repository provides a **GitHub Action** to post an SFW anime GIF to a Slack channel of your choice.
The reference set of GIFs is defined at https://github.com/LTLA/acceptable-anime-gifs.

If you have already set up a [Slack app](https://api.slack.com/apps),
you can define an incoming webhook to the desired channel and use it in your Action.
This assumes that the webhook URL is saved as a secret in the repository.

```yaml
- name: Post anime GIF 
  uses: LTLA/actions-anime-gif-slackbot@master
  with:
    webhook: ${{ secrets.SLACK_WORK_WEBHOOK }}
```

You can control the [sentiments](https://ltla.github.io/acceptable-anime-gifs/sentiment/) of the GIFs
and the maximum safe-for-work rating (0 being safest, 4 being... less so) with:

```yaml
- name: Post celebratory and kide-safe GIF 
  uses: LTLA/actions-anime-gif-slackbot@master
  with:
    webhook: ${{ secrets.SLACK_WORK_WEBHOOK }}
    sentiment: thumbs_up,celebrate
    rating: 1
```
