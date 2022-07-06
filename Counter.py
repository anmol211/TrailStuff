from collections import Counter

# take no. of test cases form user
test_cases = int(input("No. of testcases"))

testcase_result = []
for test in range(test_cases):
    # for each testcase, take no. of tweets from user
    tweets_count = int(input("No. of tweets"))
    tweets = []
    # take input tweet based on no of tweets
    for tweet in range(tweets_count):
        tweets.append(input("Enter the tweet").split()[0])

    # Calculate the max tweet users using Counter
    result_list = Counter(tweets)
    max_number = max(result_list.values())
    # sort result for alphabetical result
    for result in sorted(result_list.keys()):
        if result_list[result] == max_number:
            testcase_result.append([result, result_list[result]])

# show the output of testcases
for testcase_output in testcase_result:
    print(testcase_output[0] + " " + str(testcase_output[1]))
