-- Prison Security System Script
-- Manages detection, alerts, and lockdown procedures

local security_level = 100
local alert_status = false
local breach_locations = {}

function detectThreat(location, threat_type)
    if threat_type == 'escape_attempt' then
        security_level = security_level - 10
        triggerAlarm(location)
        table.insert(breach_locations, location)
    elseif threat_type == 'contraband' then
        security_level = security_level - 5
    end
end

function triggerAlarm(location)
    alert_status = true
    return {
        alert = true,
        location = location,
        timestamp = os.time()
    }
end

function updateSecurityStatus()
    if security_level < 30 then
        initiateFullLockdown()
    end
    return security_level
end

function initiateFullLockdown()
    local lockdown_config = {
        all_doors_locked = true,
        surveillance_active = true,
        patrol_increased = true,
        visitation_suspended = true
    }
    return lockdown_config
end

function getSecurity Status()
    return security_level
end
