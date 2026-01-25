"""Shared constants for the Gate Entry module."""

from __future__ import annotations

INBOUND_REFERENCES = frozenset({"Purchase Order", "Subcontracting Order"})
OUTBOUND_REFERENCES = frozenset({"Sales Invoice", "Delivery Note"})
ALL_REFERENCES = INBOUND_REFERENCES | OUTBOUND_REFERENCES | {"Stock Entry"}

REFERENCE_PARTY_FIELDS = {
	"Purchase Order": ("supplier", "supplier_name"),
	"Subcontracting Order": ("supplier", "supplier_name"),
	"Sales Invoice": ("customer", "customer_name"),
	"Delivery Note": ("customer", "customer_name"),
}

REFERENCE_TOTAL_FIELDS = (
	"rounded_total",
	"grand_total",
	"base_grand_total",
	"net_total",
	"total",
	"base_total",
)
