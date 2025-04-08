# API Best Practices Guidelines [Coding Practice]
<font size="-1">_Author: Frank Arana - Dec. 2018_</font>

## Overview

This document covers general security guidelines for API endpoints within Unity. These guidelines will cover general points like:
- [Access control best practices](#access-controls)
- [Input validation](#input-validation)
- [Request verification](#request-integrity)
- [Replay attacks](#replay-attacks)
- [General security practices relevant to, but not specific to APIs](#general)

---

### Recommendations

#### Access Controls

###### Description  
API endpoints should follow the principle of least privilege. Services with protected information should serve to the smallest group possible.

###### Why We Care  
APIs with misconfigured access controls can lead to unintentional information leaks, or unauthorized and malicious state-changing actions on sensitive data.

###### Example of Issue (Optional)  
- A POST that allows the user to modify information on an account without checking if the user owns the account being modified.  
- A GET request that returns sensitive informative information without authentication.

###### How to Fix?  
- Determine which API actions should be considered sensitive or public.  
- For internal APIs: restrict to internal networks and use strong authentication (e.g., MFA).  
- For public APIs with sensitive data: require authentication, use revocable and renewable API keys.  
- For public APIs with public info: avoid state-changing actions, apply rate limiting.

###### Risk Rating  
Incorrect access controls can range from High to Low Severity.

###### References (Optional)  
- https://www.owasp.org/index.php/REST_Security_Cheat_Sheet

---

#### Input Validation

###### Description  
Incoming data can be malformed or crafted to cause unintended behavior when it is parsed.

###### Why We Care  
Unvalidated input can include command injections, XSS attacks, or other harmful actions.

###### Example of Issue (Optional)  
Un formulario de contacto permite enviar datos con `script` embebido, como:

```html
<input name="email" value="<script>alert('XSS')</script>">
```

###### How to Fix?  
- Type checking  
- Length and size limits  
- Whitelist accepted content-types  
- Restrict HTTP methods  
- Keep third-party parsers updated and review changes to internal parsers

###### Risk Rating  
Can range from Low to High depending on severity and usage.

---

### Request Integrity

###### Description  
It is possible that a request could be modified in-transit between the original requestor and the API endpoint.

###### Why We Care  
Modified requests may alter data, result in incorrect responses, or perform unintended actions.

###### Example of Issue (Optional)  
*TBD*

###### How to Fix?  
- Sign requests with HMACs  
- Include timestamps  
- Reject outdated requests  
- Use HTTPS to avoid data being tampered with

###### Risk Rating  
Varies depending on what data/actions the request contains.

---

### Replay Attacks

###### Description  
An attacker sends a previously valid request to trigger the same action again.

###### How to Fix?  
 Arreglandolo :v

###### Risk Rating  
Severity depends on the impact of repeated requests.

###### References (Optional)  
- https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html#why-requests-are-signed

---

### General

###### Description  
Common security practices relevant to APIs and web services in general.

###### Why We Care  
Even with proper API rules, poor overall security may leave vulnerabilities.

###### Example of Issue (Optional)  
- Lack of logging and monitoring  
- Returning full stack traces or sensitive debug data in errors

###### How to Fix?  
- Log and monitor API activity to detect anomalies  
- Disable or limit CORS  
- Use vague error messages—avoid exposing internal server or debug info

###### Risk Rating  
Ranging from Low to High depending on the situation.