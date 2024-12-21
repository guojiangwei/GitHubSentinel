class ReportGenerator:
    def generate_report(self, updates):
        report = "### GitHub Repository Updates\n"
        for (owner, name), update in updates.items():
            report += f"#### {owner}/{name}\n"
            for event in update:
                report += f"- {event['type']} on {event['created_at']}\n"
        return report
