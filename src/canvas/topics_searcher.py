import requests
import json
from datetime import datetime, timedelta
import re
import pandas as pd
import yaml

with open(r'./credentials.yaml') as file:
        parameters = yaml.load(file, Loader=yaml.FullLoader)

bearer_token = parameters['bearer_token']
base_url = parameters['base_url']
header = {'Authorization': 'Bearer ' + bearer_token}
mentor_list = parameters['mentor_list']

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  cleantext = re.sub('\n', '', cleantext)
  return cleantext

def get_courses_list():
  url_courses = '/api/v1/courses?per_page=10000'
  response = requests.get(base_url+url_courses, headers=header)
  courses = response.json()
  return list(course['id'] for course in courses)


def get_courses_list_name():
  url_courses = '/api/v1/courses?per_page=10000'
  response = requests.get(base_url+url_courses, headers=header)
  courses = response.json()
  return list(course['name'] for course in courses)


def get_discussion_topics(course):
  topics_url = '/api/v1/courses/{}/discussion_topics'.format(course)
  response = requests.get(base_url+topics_url, headers=header)
  return [[course, topic['id'], topic['url']] for topic in response.json()]

def get_discussion_topics_details(course, topic_id):
  # read_state
  # user_id3
  try:
    topic_entries_url = '/api/v1/courses/{}/discussion_topics/{}/entries'.format(course, topic_id)
    response = requests.get(base_url+topic_entries_url, headers=header)
    topics_entries = response.json()

    return [filter_discussion_topics_details(topic_entry) for topic_entry in topics_entries if len(topic_entry)>0]
  except:
    pass

def filter_discussion_topics_details(json_topic):
    #Unnesting dictionary
    last_period = datetime.strftime(datetime.now() - timedelta(30), '%Y-%m-%dT00:00:00Z')
    try:
        replies = json_topic['recent_replies']
        replies_number = len(replies)
        mentor_intervention = False
        last_update = max([update['created_at'] for update in replies])
        interaction_list = [reply['user']['id'] for reply in replies if reply['user']['id'] in mentor_list]
                            #reply['created_at'] == last_update
                            
        if((len(interaction_list) == 0 or replies_number == 0) and json_topic['created_at'] > last_period):
            return [json_topic['created_at'], cleanhtml(json_topic['message']), json_topic['user_name']]
    except:
        pass

def execute():
    try:
        columns = ['course', 'topic', 'url', 'created_at', 'message', 'user_name']
        final_df = pd.DataFrame()
        courses_list = get_courses_list()
        for course in courses_list:
            topics = pd.DataFrame(get_discussion_topics(course), columns=['course', 'topic', 'url'])
            if(len(topics)>0):
                for index,row in topics.iterrows():
                    filtered_results = get_discussion_topics_details(row['course'], row['topic'])
                    if(filtered_results):
                        if(len(filtered_results)>0):
                            for result in filtered_results:
                                if(result is not None):
                                    final_df = final_df.append([[row['course'], row['topic'], row['url']]+result])
        final_df.columns = columns
        return(final_df)
    except:
        return None