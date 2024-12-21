import smtplib
import requests

class NotificationSystem:
    def __init__(self, config):
        self.config = config

    def send_email(self, subject, body):
        # 使用 SMTP 发送邮件
        with smtplib.SMTP("smtp.example.com") as server:
            server.login(self.config["email_user"], self.config["email_password"])
            message = f"Subject: {subject}\n\n{body}"
            server.sendmail(self.config["email"], self.config["email"], message)

    def send_slack_notification(self, message):
        # 使用 Slack Webhook 发送消息
        payload = {"text": message}
        requests.post(self.config["slack_webhook"], json=payload)

    def send_update(self, updates):
        message = "\n".join([f"Repo: {owner}/{name}\nUpdates: {update}" 
                             for (owner, name), update in updates.items()])
        self.send_email("GitHub Repo Updates", message)
        self.send_slack_notification(message)
