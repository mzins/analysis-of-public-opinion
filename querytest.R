# downloading academictwitteR and try to use Madelaine's query 
install.packages("academictwitteR")
library(academictwitteR)

# https://twittercommunity.com/t/r-twitter-account-authentication/163021
consumer_key="2D9iblmd97zASdKcf7C2B5Cvs"
consumer_secret="L7RdTAQw0FQpUmFJy8FP8r8eodqhoEe2omckwhUVr7ECeSYODB"
bearer_token="AAAAAAAAAAAAAAAAAAAAAD%2FBigEAAAAA3yv7Gkpj%2FtNFMOC%2Fay%2FQSGefwQM%3D9i5F8nljDBwiXj2xotacMg9dob4qLJnkFFj3pmXHcLrmBqTcSV"
access_token="1586060936774819840-E8ZwiHmWnWCNRrvGwXsXxOaJEZxZMy"
access_token_secret="QVGtwGet4bXQAEsfMUtDsy2p1vlZfhP0dTxNfSbu661wf"

# twitter_token <- create_token(
#   app = "student-loan-sentiment",
#   consumer_key = consumer_key,
#   consumer_secret = consumer_secret,
#   access_token = access_token,
#   access_secret = access_secret)
# 
# twitter_token

setup_twitter_oauth(consumer_key, consumer_secret, access_token, access_token_secret)


bearer_token_here = bearer_token="AAAAAAAAAAAAAAAAAAAAAD%2FBigEAAAAA3yv7Gkpj%2FtNFMOC%2Fay%2FQSGefwQM%3D9i5F8nljDBwiXj2xotacMg9dob4qLJnkFFj3pmXHcLrmBqTcSV"
q = c("student loan forgiveness","student loans", "student loan", "student debt", "loan forgiveness","debt forgiveness", "biden student loan") 

# query:  (student loan forgiveness OR student loans OR student loan OR student debt OR loan forgiveness OR debt forgiveness OR biden student loan) 
# (to:usedgov OR to:foxnews OR to:cnn OR to:msnbc OR to:nytimes) 


test_query = build_query(
  # query = c("student loan forgiveness","student loans", "student loan",
  #           "student debt", "loan forgiveness",
  #           "debt forgiveness", "biden student loan") ,
  query = c("student loan")
  exact_phrase = TRUE,
  users = NULL,
  reply_to = c("usedgov", "foxnews", "cnn", "msnbc", "nytimes"),
  retweets_of = NULL,
  exclude = NULL,
  is_retweet = FALSE, # <--
  is_reply = TRUE, # <--
  is_quote = NULL,
  is_verified = NULL,
  remove_promoted = FALSE,
  has_hashtags = NULL,
  has_cashtags = NULL,
  has_links = FALSE, # <-- 
  has_mentions = NULL,
  has_media = NULL,
  has_images = NULL,
  has_videos = NULL,
  has_geo = NULL,
  place = NULL,
  country = NULL,
  point_radius = NULL,
  bbox = NULL,
  lang = NULL,
  conversation_id = NULL,
  url = NULL
)




# ["usedgov", "foxnews", "cnn"]: # add msnbc, nytimes, npr
tweets = get_all_tweets(query = q, 
               start_tweets = "2022-12-01T00:00:00Z", 
               end_tweets = "2020-12-05T00:00:00Z", 
               bearer_token = bearer_token_here, #get_bearer(), 
               #reply_to = c("usedgov", "foxnews", "cnn", "msnbc", "nytimes"), 
               data_path = "data/",
               n = 500)

# https://cran.r-project.org/web/packages/academictwitteR/vignettes/academictwitteR-intro.html
tweets <-
  get_all_tweets(
    query = "#BlackLivesMatter",
    bearer_token = bearer_token_here,
    start_tweets = "2020-01-01T00:00:00Z",
    end_tweets = "2020-01-05T00:00:00Z",
    file = "blmtweets"
  )







# https://www.infoworld.com/article/3515712/how-to-search-twitter-with-rtweet-and-r.html
# # trying out with rtweet =====
install.packages("rtweet")
library(rtweet)
# setup_twitter_oauth(consumer_key, consumer_secret, access_token, access_secret)
auth_setup_default()

q_val3 = "(student loan) (to:usedgov OR to:foxnews OR to:cnn OR to:msnbc OR to:nytimes) 
-filter:retweet filter:replies -has:links"

q_val4 = "(\"student loan forgiveness\" OR \"student loan\" OR \"student debt\" OR \"loan forgiveness\" OR \"debt forgiveness\" OR \"biden student loan\") 
(to:usedgov OR to:foxnews OR to:cnn OR to:msnbc OR to:nytimes) -filter:retweet filter:replies -has:links"

tweet_df3 <- search_tweets2(q = q_val4, n = 10, 
                          include_rts = FALSE)




