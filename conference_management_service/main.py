import argparse
from injector import Injector
from di.config import ConfigModule
from presentation.app import InstantTranslationApp
class CliApp:
    def __init__(self, injector):
        # Argument parser to handle CLI commands and options
        self.parser = argparse.ArgumentParser(description="CLI for InstantTranslationApp.")
        self.parser.add_argument(
            "command", choices=["start", "help", "migrate"], help="Command to run."
        )
        self.parser.add_argument(
            "--api-host",
            default="127.0.0.1",
            help="Host to run the REST api (default: 127.0.0.1)"
        )
        self.parser.add_argument(
            "--api-port",
            type=int,
            default=8000,
            help="Port to run the REST api (default: 8000)"
        )
        self.parser.add_argument(
            "--messaging-host",
            default="127.0.0.1",
            help="Host of the NATS server (default: 127.0.0.1)"
        )
        self.parser.add_argument(
            "--messaging-port",
            type=int,
            default=4222,
            help="Port of the NATS server (default: 4222)"
        )
        self.parser.add_argument(
            "--vad-host",
            default="127.0.0.1",
            help="Host of the VAD server (default: 127.0.0.1)"
        )
        self.parser.add_argument(
            "--vad-port",
            type=int,
            default=4222,
            help="Port of the VAD server (default: 4222)"
        )
        self.parser.add_argument(
            "--translation-host",
            default="127.0.0.1",
            help="Host of the Translation server (default: 127.0.0.1)"
        )
        self.parser.add_argument(
            "--translation-port",
            type=int,
            default=7860,
            help="Port of the Translation server (default: 7860)"
        )
        self.injector = injector  # Injector instance
        self.app: InstantTranslationApp = self.injector.get(InstantTranslationApp)

    def start(self, args):
        """Run the InstantTranslationApp with the provided arguments."""
        # Instantiate your Api and MessagingInterface objects
        # Run the app using uvicorn with the provided host and port
        self.app.start(
            api_host=args.api_host,
            api_port=args.api_port,
            messaging_host=args.messaging_host,
            messaging_port=args.messaging_port,
            vad_host=args.vad_host,
            vad_port=args.vad_port,
            translation_host=args.translation_host,
            translation_port=args.translation_port,
        )

    def help(self):
        """Display help information."""
        self.parser.print_help()
        
    def migrate(self):
        """Migrate db."""
        self.app.migrate()

    def run(self):
        """Parse CLI arguments and run the appropriate command."""
        args = self.parser.parse_args()

        if args.command == "start":
            self.start(args)
        elif args.command == "help":
            self.help(args)
        elif args.command == "migrate":
            self.migrate()


# Main entry point for the CLI
if __name__ == "__main__":
    injector_instance = Injector(ConfigModule())
    cli = CliApp(injector_instance)
    cli.run()
