-- 1. What query would you run to get all tweets from the user id of 1?

SELECT *
FROM users 
LEFT JOIN tweets
ON users.id = tweets.user_id
WHERE users.id = 1; 

SELECT tweets.tweet as kobe_tweets
FROM users 
LEFT JOIN tweets 
ON users.id = tweets.user_id 
WHERE users.id = 1; 

-- 2. What query would return all the tweets that the user with id 2 has tagged as favorites?
SELECT first_name, tweet  
FROM users 
LEFT JOIN faves 
ON faves.user_id = users.id 
LEFT JOIN tweets 
ON tweets.id = faves.tweet_id 
WHERE users.id =1 OR users.id=2; 

-- 4.What query would you run to get all the users that are following the user with id 1?
SELECT users.id as FOLLOWED_ID, users.first_name as FOLLOWED_FIRSTNAME, users2.first_name as FOLLOWER
FROM users 
LEFT JOIN follows 
ON follows.followed_id = users.id 
LEFT JOIN users as users2
ON users2.id = follows.follower_id 
WHERE users.id = 1





