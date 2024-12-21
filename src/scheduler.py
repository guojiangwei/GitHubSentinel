import schedule
import time

class Scheduler:
    def __init__(self, subscription_manager, notification_system, report_generator):
        self.subscription_manager = subscription_manager
        self.notification_system = notification_system
        self.report_generator = report_generator

    def schedule_tasks(self):
        schedule.every().day.at("12:00").do(self.run_daily_tasks)

        while True:
            schedule.run_pending()
            time.sleep(1)

    def run_daily_tasks(self):
        updates = self.subscription_manager.fetch_updates_for_all()
        report = self.report_generator.generate_report(updates)
        self.notification_system.send_update(updates)
