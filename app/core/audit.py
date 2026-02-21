import asyncio
from datetime import datetime, timezone

from supabase import Client


class AuditLogger:
    """Async, non-blocking audit logger writing to Supabase audit_logs table."""

    def __init__(self, supabase_client: Client):
        self.client = supabase_client

    async def log_event(
        self,
        user_id: str,
        action: str,
        resource_type: str,
        resource_id: str | None = None,
        metadata: dict | None = None,
        ip_address: str | None = None,
    ) -> None:
        """Fire-and-forget audit log write. Never blocks the request path."""
        entry = {
            "user_id": user_id,
            "action": action,
            "resource_type": resource_type,
            "resource_id": resource_id,
            "metadata": metadata or {},
            "ip_address": ip_address,
            "created_at": datetime.now(timezone.utc).isoformat(),
        }
        try:
            asyncio.create_task(self._write(entry))
        except Exception:
            pass  # Audit failure must never block primary operation

    async def _write(self, entry: dict) -> None:
        self.client.table("audit_logs").insert(entry).execute()
