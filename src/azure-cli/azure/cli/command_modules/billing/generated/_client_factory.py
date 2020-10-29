# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_billing_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azure.mgmt.billing import BillingManagementClient
    return get_mgmt_service_client(cli_ctx,
                                   BillingManagementClient)


def cf_account(cli_ctx, *_):
    return cf_billing_cl(cli_ctx).billing_accounts


def cf_balance(cli_ctx, *_):
    return cf_billing_cl(cli_ctx).available_balances


def cf_profile(cli_ctx, *_):
    return cf_billing_cl(cli_ctx).billing_profiles


def cf_customer(cli_ctx, *_):
    return cf_billing_cl(cli_ctx).customers


def cf_invoice_section(cli_ctx, *_):
    return cf_billing_cl(cli_ctx).invoice_sections


def cf_subscription(cli_ctx, *_):
    return cf_billing_cl(cli_ctx).billing_subscriptions


def cf_product(cli_ctx, *_):
    return cf_billing_cl(cli_ctx).products


def cf_invoice(cli_ctx, *_):
    return cf_billing_cl(cli_ctx).invoices


def cf_transaction(cli_ctx, *_):
    return cf_billing_cl(cli_ctx).transactions


def cf_policy(cli_ctx, *_):
    return cf_billing_cl(cli_ctx).policies


def cf_property(cli_ctx, *_):
    return cf_billing_cl(cli_ctx).billing_property