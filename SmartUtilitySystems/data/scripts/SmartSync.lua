local timeTot = 0

function Create()
  timeTot = 20
end

function Update(timePassed)
  timeTot = timeTot + timePassed
  if timeTot >= 30 then
    timeTot = 0
    RunSyncLogic()
  end
end

function RunSyncLogic()
  -- Scanner Logic
  local scanners = World.GetNearbyObjects('ScannerMachine', 50)
  local monitors = World.GetNearbyObjects('Monitor', 50)
  
  if scanners and monitors and #monitors > 0 then
    for i, scan in pairs(scanners) do
      local isWired = false
      local conns = scan.GetConnections()
      
      if conns then
        for k, v in pairs(conns) do
          if v.Type == "Monitor" then
            isWired = true
          end
        end
      end
      
      if not isWired then
        Object.Connect(scan, monitors[1])
      end
    end
  end
  
  -- Door Servo Logic
  local servos = World.GetNearbyObjects('DoorServo', 30)
  local controls = World.GetNearbyObjects('DoorControlSystem', 9999)
  
  if servos and controls and #controls > 0 then
    for i, servo in pairs(servos) do
      local isWired = false
      local conns = servo.GetConnections()
      
      if conns then
        for k, v in pairs(conns) do
          if v.Type == "DoorControlSystem" then
            isWired = true
          end
        end
      end
      
      if not isWired then
        Object.Connect(servo, controls[1])
      end
    end
  end
end
