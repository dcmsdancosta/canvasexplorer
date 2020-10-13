import os
import canvas.topics_searcher as ts
import trello.card_creator as cc
import yaml

def main():
    issues = ts.execute()
    cc.executeIssues(issues)

if __name__ == '__main__':
    main()