import unittest
from copy import deepcopy

from openprocurement.auctions.core.tests.base import snitch

from openprocurement.auctions.appraisal.tests.base import (
    BaseAppraisalAuctionWebTest,
    test_appraisal_auction_data,
    test_appraisal_item_data
)
from openprocurement.auctions.appraisal.tests.blanks.item_blanks import (
    check_item_creation,
    check_items_listing,
    check_item_patch,
    check_patch_auction_in_not_editable_statuses,
    validate_change_items_after_rectification_period,
    batch_create_items,
    batch_update_items,
    check_bids_invalidation
)

test_auction_data = deepcopy(test_appraisal_auction_data)


class AppraisalAuctionItemTest(BaseAppraisalAuctionWebTest):

    initial_data = test_auction_data
    initial_item_data = deepcopy(test_appraisal_item_data)

    test_check_items_listing = snitch(check_items_listing)
    test_check_item_creation = snitch(check_item_creation)
    test_check_item_patch = snitch(check_item_patch)
    test_check_patch_auction_in_not_editable_statuses = snitch(check_patch_auction_in_not_editable_statuses)
    test_validate_change_items_after_rectification_period = snitch(validate_change_items_after_rectification_period)
    test_batch_create_items = snitch(batch_create_items)
    test_batch_update_items = snitch(batch_update_items)
    test_check_bids_invalidation = snitch(check_bids_invalidation)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(AppraisalAuctionItemTest))
    return suite
