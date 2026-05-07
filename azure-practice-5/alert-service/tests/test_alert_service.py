from alert_service.services.feedback_service import send_feedback

def test_send_feedback_returns_success():
    result = send_feedback("test message")

    assert result is True or result is None