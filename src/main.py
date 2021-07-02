import os
import canvas.topics_searcher as ts
import trello.card_creator as cc
import yaml

def main():
    issues = ts.execute()
    if(issues is not None):
        cc.executeIssues(issues)

if __name__ == '__main__':
    main()