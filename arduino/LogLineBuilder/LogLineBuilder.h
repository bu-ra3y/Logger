// LogLineBuilder.h
// 
//
#ifndef LogLineBuilder_h
#define LogLineBuilder_h

#include "Arduino.h"

class LogLineBuilder {
  public: 
  	LogLineBuilder();
  	void put(String key, String value);
	void put(String key, int value);
	void put(String key, long value);
  	String getLine();
  private:
  	String _s;
};

#endif