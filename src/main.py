from github_api import GitHubAPI
from subscription import SubscriptionManager
from notification import NotificationSystem
from report import ReportGenerator
from scheduler import Scheduler
from config import Config

def main():
    config = Config.load()
    
    github_api = GitHubAPI(config['github_token'])
    subscription_manager = SubscriptionManager(github_api)
    notification_system = NotificationSystem(config['notification_config'])
    report_generator = ReportGenerator()
    scheduler = Scheduler(subscription_manager, notification_system, report_generator)

    # 启动调度任务
    scheduler.schedule_tasks()

if __name__ == "__main__":
    main()
