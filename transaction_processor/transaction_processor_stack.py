from aws_cdk import core
from aws_cdk import aws_lambda as lambda_
from aws_cdk import aws_sns as sns
from aws_cdk import aws_sns_subscriptions as subscription
from aws_cdk import aws_stepfunctions as sfn
from aws_cdk import aws_stepfunctions_tasks as tasks
from aws_cdk import aws_secretsmanager as secrets
from aws_cdk import aws_events as events
from aws_cdk import aws_events_targets as targets
from aws_cdk import aws_s3 as s3
import aws_cdk.aws_secretsmanager as sm
from cdk_watchful import Watchful
from aws_cdk.aws_events import Rule, Schedule
from aws_cdk.core import Duration


class TransactionProcessorStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
         
        ProcessPurchase = lambda_.Function(self, 'process-purchase', 
                                            runtime=lambda_.Runtime.PYTHON_3_8,
                                            handler='handler.process_purchase',
                                            code=lambda_.Code.from_asset('./code'),
                                            timeout=(Duration.seconds(5)))                               

        ProcessRefund = lambda_.Function(self, 'process-refund', 
                                            runtime=lambda_.Runtime.PYTHON_3_8,
                                            handler='handler.process_refund',
                                            code=lambda_.Code.from_asset('./code'),
                                            timeout=(Duration.seconds(5)))

        GeneratePurchaseReceipt = lambda_.Function(self, 'generate-purchase-receipt', 
                                                    runtime=lambda_.Runtime.PYTHON_3_8,
                                                    handler='handler.generate_purchase_receipt',
                                                    code=lambda_.Code.from_asset('./code'),
                                                    timeout=(Duration.seconds(5)))                               

        GenerateRefundReceipt = lambda_.Function(self, 'generate-refund-receipt', 
                                                    runtime=lambda_.Runtime.PYTHON_3_8,
                                                    handler='handler.generate_refund_receipt',
                                                    code=lambda_.Code.from_asset('./code'),
                                                    timeout=(Duration.seconds(5)))




        ProcessPurchaseState = tasks.LambdaInvoke(self, 'process purchase task',
                                                lambda_function=ProcessPurchase,
                                                input_path='$')

        ProcessRefundState = tasks.LambdaInvoke(self, 'process refund task',
                                                lambda_function=ProcessRefund,
                                                input_path='$')

        GeneratePurchaseReceiptState = tasks.LambdaInvoke(self, 'generate purchase receipt',
                                                        lambda_function=GeneratePurchaseReceipt,
                                                        input_path='$')

        GenerateRefundReceiptState = tasks.LambdaInvoke(self, 'generate refund receipt',
                                                        lambda_function=GenerateRefundReceipt,
                                                        input_path='$')       

        TransactionChoice = sfn.Choice(self, 'process transaction',
                                        output_path='$')

        TransactionTypeEqualsPurchase = sfn.Condition.string_equals('$.TransactionType', 'PURCHASE')
        TransactionTypeEqualsRefund = sfn.Condition.string_equals('$.TransactionType', 'REFUND')

        # StateMachineDefinition = TransactionChoice.when(TransactionTypeEqualsPurchase, ProcessPurchaseState).when(TransactionTypeEqualsRefund, ProcessRefundState) # works 
        StateMachineDefinition = TransactionChoice.when(TransactionTypeEqualsPurchase, ProcessPurchaseState.next(GeneratePurchaseReceiptState)).when(TransactionTypeEqualsRefund, ProcessRefundState.next(GenerateRefundReceiptState))

        Workflow = sfn.StateMachine(self, 'transaction workflow', definition=StateMachineDefinition)

        

        


        
