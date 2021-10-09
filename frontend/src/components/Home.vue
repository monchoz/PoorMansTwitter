<template>
  <div>
    <h1 class="title">Poor Man's Twitter</h1>
    <form>
      <h2 class="subtitle">Add your Tweet</h2>
      <div class="field">
        <label class="label">Name</label>
        <div class="control">
          <input v-model="name" class="input" type="text" required>
        </div>
      </div>
      <div class="field">
        <label class="label">Message</label>
        <div class="control">
          <textarea v-model="message" class="message" maxlength="50" required>
          </textarea>
        </div>
      </div>
      <div class="field">
        <div class="control">
          <button class="submit" @click="addTweet()">Send</button>
        </div>
      </div>
    </form>
    <div class="tweets">
      <div class="tweet" v-for="tweet in tweets">
        <span class="tweet__name">{{ tweet.name }}</span>
        <span class="tweet__message">{{ tweet.message }}</span>
        <span class="tweet__datetime">{{ tweet.datetime }}</span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Home',
  data () {
    return {
      tweets: [],
      name: '',
      message: ''
    }
  },
  mounted() {
    this.getTweets()
  },
  methods: {
    getTweets() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/tweets/'
      }).then(response => this.tweets = response.data)
    },
    addTweet() {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/tweets/',
        data: {
          name: this.name,
          message: this.message
        }
      }).then((response) => {
        this.tweets({
          'name': response.data.name,
          'message': response.data.message,
          'datetime': response.data.datetime
        })
        this.name = '';
        this.message = '';
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
