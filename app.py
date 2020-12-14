#!/usr/bin/env python3

from aws_cdk import core

from transaction_processor.transaction_processor_stack import TransactionProcessorStack


app = core.App()
TransactionProcessorStack(app, "transaction-processor")

app.synth()
