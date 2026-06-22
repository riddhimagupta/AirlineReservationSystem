import shutil
import os

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

class BackupManager:

    def create_backup(self):

        if not os.path.exists("backups"):
            os.mkdir("backups")

        shutil.copy(
            os.path.join(BASE_DIR, "routes.json"),
            os.path.join(
                BASE_DIR,
                "backups",
                "routes_backup.json"
            )
        )

        shutil.copy(
           os.path.join(BASE_DIR, "bookings.json"),
            os.path.join(
                BASE_DIR,
                "backups",
                "bookings_backup.json"
            )
        )

        shutil.copy(
            os.path.join(BASE_DIR, "seats.json"),
            os.path.join(
                BASE_DIR,
                "backups",
                "seats_backup.json"
            )
        )

        shutil.copy(
            os.path.join(BASE_DIR, "cancellations.json"),
            os.path.join(
                BASE_DIR,
                "backups",
                "cancellations_backup.json"
            )
        )

    def restore_backup(self):

        shutil.copy(
            "backups/routes_backup.json",
            "routes.json"
        )

        shutil.copy(
            "backups/bookings_backup.json",
            "bookings.json"
        )

        shutil.copy(
            "backups/seats_backup.json",
            "seats.json"
        )

        shutil.copy(
            "backups/cancellations_backup.json",
            "cancellations.json"
        )